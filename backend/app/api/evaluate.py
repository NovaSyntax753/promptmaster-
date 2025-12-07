from fastapi import APIRouter, HTTPException, Header
from app.models.schemas import PromptSubmission, EvaluationResult
from app.services.evaluation_service import EvaluationService
from typing import List, Optional

router = APIRouter()
evaluation_service = EvaluationService()


@router.post("/", response_model=EvaluationResult)
async def evaluate_prompt(
    submission: PromptSubmission,
    authorization: str = Header(None)
):
    """
    Submit a prompt for evaluation and get scores with improvement suggestions.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header required")
    
    try:
        # Extract token from "Bearer <token>"
        token = authorization.replace("Bearer ", "")
        
        result = await evaluation_service.evaluate_prompt(
            user_token=token,
            challenge_id=submission.challenge_id,
            user_prompt=submission.user_prompt
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history", response_model=List[EvaluationResult])
async def get_evaluation_history(
    authorization: str = Header(None),
    limit: int = 10,
    offset: int = 0,
    challenge_id: Optional[int] = None
):
    """
    Get user's evaluation history.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header required")
    
    try:
        token = authorization.replace("Bearer ", "")
        
        history = await evaluation_service.get_user_history(
            user_token=token,
            limit=limit,
            offset=offset,
            challenge_id=challenge_id
        )
        return history
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{evaluation_id}", response_model=EvaluationResult)
async def get_evaluation(
    evaluation_id: int,
    authorization: str = Header(None)
):
    """
    Get a specific evaluation by ID.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header required")
    
    try:
        token = authorization.replace("Bearer ", "")
        
        evaluation = await evaluation_service.get_evaluation_by_id(
            evaluation_id=evaluation_id,
            user_token=token
        )
        
        if not evaluation:
            raise HTTPException(status_code=404, detail="Evaluation not found")
        
        return evaluation
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
