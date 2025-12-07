from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.api import auth, challenges, evaluate, progress
import logging
import traceback

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Test & Improve Your Prompting Skills",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global exception handler to prevent server crashes
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Catch all unhandled exceptions to prevent server crashes."""
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    logger.error(f"Request URL: {request.url}")
    logger.error(f"Traceback: {traceback.format_exc()}")
    
    # Return a proper error response instead of crashing
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error. Please try again later.",
            "error_type": type(exc).__name__
        }
    )

# Include routers
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(challenges.router, prefix=f"{settings.API_V1_STR}/challenges", tags=["challenges"])
app.include_router(evaluate.router, prefix=f"{settings.API_V1_STR}/evaluate", tags=["evaluate"])
app.include_router(progress.router, prefix=f"{settings.API_V1_STR}/progress", tags=["progress"])


@app.get("/")
async def root():
    return {
        "message": "Welcome to PromptMaster API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/debug/env")
async def debug_env():
    """Debug endpoint to check environment variables"""
    return {
        "supabase_url": settings.SUPABASE_URL[:30] + "..." if settings.SUPABASE_URL else "NOT SET",
        "supabase_key_length": len(settings.SUPABASE_KEY) if settings.SUPABASE_KEY else 0,
        "cors_origins": settings.BACKEND_CORS_ORIGINS
    }


@app.get("/debug/auth")
async def debug_auth(authorization: str = None):
    """Debug endpoint to test auth"""
    from app.services.auth_service import AuthService
    
    if not authorization:
        return {"error": "No authorization header"}
    
    try:
        token = authorization.replace("Bearer ", "")
        auth_service = AuthService()
        user = await auth_service.get_user(token)
        return {
            "success": True,
            "user_id": user.id,
            "email": user.email
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
