from fastapi import APIRouter, HTTPException, Header
from app.models.schemas import DashboardStats, ProgressTrend, TopMistake
from app.services.progress_service import ProgressService
from typing import List
import logging

logger = logging.getLogger(__name__)

router = APIRouter()
progress_service = ProgressService()


@router.get("/dashboard", response_model=DashboardStats)
async def get_dashboard_stats(authorization: str = Header(None)):
    """
    Get user's dashboard statistics including total attempts, average score, and improvement.
    """
    try:
        logger.info(f"Dashboard endpoint called with auth: {authorization[:30] if authorization else 'None'}...")
        
        if not authorization:
            raise HTTPException(status_code=401, detail="Authorization header required")
        
        token = authorization.replace("Bearer ", "")
        logger.info(f"Token extracted: {token[:20]}...")
        
        stats = await progress_service.get_dashboard_stats(token)
        logger.info(f"Stats retrieved successfully: {stats}")
        return stats
    except HTTPException as he:
        logger.error(f"HTTP Exception in dashboard: {he.detail}")
        raise he
    except Exception as e:
        logger.error(f"Error in dashboard endpoint: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/trends", response_model=List[ProgressTrend])
async def get_progress_trends(
    authorization: str = Header(None),
    days: int = 30
):
    """
    Get user's progress trends over time.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header required")
    
    try:
        token = authorization.replace("Bearer ", "")
        trends = await progress_service.get_progress_trends(token, days)
        return trends
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/mistakes", response_model=List[TopMistake])
async def get_top_mistakes(authorization: str = Header(None)):
    """
    Get user's top 3 most common mistakes based on feedback frequency.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header required")
    
    try:
        token = authorization.replace("Bearer ", "")
        mistakes = await progress_service.get_top_mistakes(token)
        return mistakes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/category/{category}")
async def get_category_stats(
    category: str,
    authorization: str = Header(None)
):
    """
    Get statistics for a specific challenge category.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header required")
    
    try:
        token = authorization.replace("Bearer ", "")
        stats = await progress_service.get_category_stats(token, category)
        return stats
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
