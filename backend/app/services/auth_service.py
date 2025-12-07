from supabase import create_client, Client
from app.core.config import settings
from app.models.schemas import UserCreate, Token, User
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class AuthService:
    def __init__(self):
        self.supabase: Client = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_KEY
        )
    
    async def sign_up(self, user_data: UserCreate) -> Token:
        """Register a new user."""
        try:
            response = self.supabase.auth.sign_up({
                "email": user_data.email,
                "password": user_data.password,
                "options": {
                    "data": {
                        "full_name": user_data.full_name
                    }
                }
            })
            
            if response.user is None:
                raise Exception("Failed to create user")
            
            user = User(
                id=response.user.id,
                email=response.user.email,
                full_name=user_data.full_name,
                created_at=datetime.now()
            )
            
            return Token(
                access_token=response.session.access_token,
                token_type="bearer",
                user=user
            )
        except Exception as e:
            raise Exception(f"Sign up failed: {str(e)}")
    
    async def sign_in(self, email: str, password: str) -> Token:
        """Login existing user."""
        try:
            response = self.supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            
            if response.user is None:
                raise Exception("Invalid credentials")
            
            user = User(
                id=response.user.id,
                email=response.user.email,
                full_name=response.user.user_metadata.get("full_name"),
                created_at=datetime.fromisoformat(response.user.created_at.replace('Z', '+00:00'))
            )
            
            return Token(
                access_token=response.session.access_token,
                token_type="bearer",
                user=user
            )
        except Exception as e:
            raise Exception(f"Sign in failed: {str(e)}")
    
    async def google_sign_in(self) -> str:
        """Initiate Google OAuth sign in."""
        try:
            response = self.supabase.auth.sign_in_with_oauth({
                "provider": "google"
            })
            return response.url
        except Exception as e:
            raise Exception(f"Google sign in failed: {str(e)}")
    
    async def get_user(self, token: str) -> User:
        """Get current user from token."""
        try:
            if not token or not token.strip():
                logger.warning("Empty token provided to get_user")
                raise Exception("Token is required")
            
            logger.info(f"Getting user with token: {token[:20]}...")
            
            # Get user from JWT token with error handling
            try:
                user_response = self.supabase.auth.get_user(token)
            except Exception as supabase_error:
                logger.error(f"Supabase auth error: {str(supabase_error)}")
                # Check if it's a token expiration or invalid token error
                error_str = str(supabase_error).lower()
                if "expired" in error_str or "invalid" in error_str or "jwt" in error_str:
                    raise Exception("Invalid or expired token. Please sign in again.")
                raise Exception(f"Authentication error: {str(supabase_error)}")
            
            if not user_response:
                logger.warning("Empty user_response from Supabase")
                raise Exception("Invalid token - no response from authentication service")
            
            if not hasattr(user_response, 'user'):
                logger.warning(f"user_response missing 'user' attribute. Type: {type(user_response)}")
                raise Exception("Invalid token - malformed response from authentication service")
            
            if not user_response.user:
                logger.warning("user_response.user is None")
                raise Exception("Invalid token - no user found")
            
            user_data = user_response.user
            
            # Validate required fields
            if not hasattr(user_data, 'id') or not user_data.id:
                logger.error("User data missing id")
                raise Exception("Invalid user data - missing user ID")
            
            if not hasattr(user_data, 'email') or not user_data.email:
                logger.error("User data missing email")
                raise Exception("Invalid user data - missing email")
            
            # Handle user_metadata safely
            full_name = None
            if hasattr(user_data, 'user_metadata') and user_data.user_metadata:
                full_name = user_data.user_metadata.get("full_name")
            
            # Handle created_at safely
            created_at = datetime.now()
            if hasattr(user_data, 'created_at') and user_data.created_at:
                try:
                    created_at_str = str(user_data.created_at).replace('Z', '+00:00')
                    created_at = datetime.fromisoformat(created_at_str)
                except (ValueError, AttributeError) as e:
                    logger.warning(f"Could not parse created_at: {e}, using current time")
                    created_at = datetime.now()
            
            return User(
                id=user_data.id,
                email=user_data.email,
                full_name=full_name,
                created_at=created_at
            )
        except Exception as e:
            logger.error(f"Error in get_user: {str(e)}", exc_info=True)
            # Re-raise with more context if it's already a formatted error
            if "Invalid" in str(e) or "expired" in str(e) or "required" in str(e):
                raise
            raise Exception(f"Failed to get user: {str(e)}")
    
    async def sign_out(self, token: str):
        """Sign out user."""
        try:
            self.supabase.auth.sign_out()
        except Exception as e:
            raise Exception(f"Sign out failed: {str(e)}")
