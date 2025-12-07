from supabase import create_client, Client
from app.core.config import settings
from app.models.schemas import Challenge
from typing import List, Optional
import random


class ChallengeService:
    def __init__(self):
        self.supabase: Client = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_KEY
        )
    
    async def get_challenges(
        self,
        category: Optional[str] = None,
        difficulty: Optional[str] = None
    ) -> List[Challenge]:
        """Get all challenges with optional filters."""
        try:
            query = self.supabase.table("challenges").select("*")
            
            if category:
                query = query.eq("category", category)
            
            if difficulty:
                # Normalize difficulty to lowercase for case-insensitive matching
                difficulty_lower = difficulty.lower()
                query = query.eq("difficulty", difficulty_lower)
            
            response = query.execute()
            
            if not response.data:
                return []
            
            return [Challenge(**challenge) for challenge in response.data]
        except Exception as e:
            raise Exception(f"Failed to fetch challenges: {str(e)}")
    
    async def get_challenge_by_id(self, challenge_id: int) -> Optional[Challenge]:
        """Get a specific challenge by ID."""
        try:
            response = self.supabase.table("challenges")\
                .select("*")\
                .eq("id", challenge_id)\
                .execute()
            
            if not response.data:
                return None
            
            return Challenge(**response.data[0])
        except Exception as e:
            raise Exception(f"Failed to fetch challenge: {str(e)}")
    
    async def get_random_challenge(self, category: Optional[str] = None) -> Optional[Challenge]:
        """Get a random challenge, optionally from a specific category."""
        try:
            challenges = await self.get_challenges(category=category)
            
            if not challenges:
                return None
            
            return random.choice(challenges)
        except Exception as e:
            raise Exception(f"Failed to fetch random challenge: {str(e)}")
