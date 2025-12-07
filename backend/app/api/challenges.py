from fastapi import APIRouter, HTTPException, Query
from app.models.schemas import Challenge
from app.services.challenge_service import ChallengeService
from typing import List, Optional

router = APIRouter()
challenge_service = ChallengeService()


@router.get("/", response_model=List[Challenge])
async def get_all_challenges(
    category: Optional[str] = None,
    difficulty: Optional[str] = None
):
    """
    Get all challenges, optionally filtered by category or difficulty.
    """
    try:
        challenges = await challenge_service.get_challenges(
            category=category,
            difficulty=difficulty
        )
        return challenges
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{challenge_id}", response_model=Challenge)
async def get_challenge(challenge_id: int):
    """
    Get a specific challenge by ID.
    """
    try:
        challenge = await challenge_service.get_challenge_by_id(challenge_id)
        if not challenge:
            raise HTTPException(status_code=404, detail="Challenge not found")
        return challenge
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/category/{category}", response_model=List[Challenge])
async def get_challenges_by_category(category: str):
    """
    Get all challenges in a specific category.
    """
    try:
        challenges = await challenge_service.get_challenges(category=category)
        return challenges
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/random/challenge", response_model=Challenge)
async def get_random_challenge(category: Optional[str] = None):
    """
    Get a random challenge, optionally from a specific category.
    """
    try:
        challenge = await challenge_service.get_random_challenge(category=category)
        if not challenge:
            raise HTTPException(status_code=404, detail="No challenges found")
        return challenge
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
