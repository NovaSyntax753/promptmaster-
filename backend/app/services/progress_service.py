from supabase import create_client, Client
from app.core.config import settings
from app.models.schemas import DashboardStats, ProgressTrend, TopMistake
from app.services.auth_service import AuthService
from typing import List
from datetime import datetime, timedelta
from collections import Counter
import logging

logger = logging.getLogger(__name__)


class ProgressService:
    def __init__(self):
        self.supabase: Client = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_KEY
        )
        self.auth_service = AuthService()
    
    async def get_dashboard_stats(self, user_token: str) -> DashboardStats:
        """Get user's dashboard statistics."""
        try:
            logger.info(f"Getting dashboard stats for token: {user_token[:20] if user_token else 'None'}...")
            
            # Get user with better error handling
            try:
                user = await self.auth_service.get_user(user_token)
                logger.info(f"User retrieved: {user.id}")
            except Exception as auth_error:
                logger.error(f"Authentication failed in get_dashboard_stats: {str(auth_error)}")
                raise Exception(f"Authentication failed: {str(auth_error)}")
            
            # Get all evaluations for user with error handling
            try:
                response = self.supabase.table("evaluations")\
                    .select("*")\
                    .eq("user_id", user.id)\
                    .execute()
                
                if not response:
                    logger.warning("No response from Supabase evaluations query")
                    evaluations = []
                else:
                    evaluations = response.data if response.data else []
                    
            except Exception as db_error:
                logger.error(f"Database error fetching evaluations: {str(db_error)}")
                # Return empty stats instead of crashing
                return DashboardStats(
                    total_attempts=0,
                    average_score=0.0,
                    improvement_rate=0.0,
                    best_category="None",
                    attempts_by_category={}
                )
            
            logger.info(f"Evaluations retrieved: {len(evaluations)}")
            
            if not evaluations:
                logger.info("No evaluations found, returning empty stats")
                return DashboardStats(
                    total_attempts=0,
                    average_score=0.0,
                    improvement_rate=0.0,
                    best_category="None",
                    attempts_by_category={}
                )
            
            # Calculate statistics with error handling
            try:
                total_attempts = len(evaluations)
                
                # Validate that evaluations have overall_score
                valid_evaluations = [e for e in evaluations if e.get("overall_score") is not None]
                if not valid_evaluations:
                    logger.warning("No evaluations with valid scores")
                    return DashboardStats(
                        total_attempts=total_attempts,
                        average_score=0.0,
                        improvement_rate=0.0,
                        best_category="None",
                        attempts_by_category={}
                    )
                
                average_score = sum(e["overall_score"] for e in valid_evaluations) / len(valid_evaluations)
                
                # Calculate improvement rate (compare first half vs second half)
                if len(valid_evaluations) >= 4:
                    mid_point = len(valid_evaluations) // 2
                    first_half_avg = sum(e["overall_score"] for e in valid_evaluations[:mid_point]) / mid_point
                    second_half_avg = sum(e["overall_score"] for e in valid_evaluations[mid_point:]) / (len(valid_evaluations) - mid_point)
                    if first_half_avg > 0:
                        improvement_rate = ((second_half_avg - first_half_avg) / first_half_avg) * 100
                    else:
                        improvement_rate = 0.0
                else:
                    improvement_rate = 0.0
                
                # Get category statistics with error handling
                category_scores = {}
                for eval in valid_evaluations:
                    try:
                        if not eval.get("challenge_id"):
                            continue
                            
                        challenge_response = self.supabase.table("challenges")\
                            .select("category")\
                            .eq("id", eval["challenge_id"])\
                            .execute()
                        
                        if challenge_response and challenge_response.data:
                            category = challenge_response.data[0].get("category")
                            if category:
                                if category not in category_scores:
                                    category_scores[category] = []
                                category_scores[category].append(eval["overall_score"])
                    except Exception as cat_error:
                        logger.warning(f"Error fetching category for challenge {eval.get('challenge_id')}: {str(cat_error)}")
                        continue
                
                attempts_by_category = {
                    cat: len(scores) for cat, scores in category_scores.items()
                }
                
                # Find best category
                if category_scores:
                    category_averages = {
                        cat: sum(scores) / len(scores)
                        for cat, scores in category_scores.items()
                    }
                    best_category = max(category_averages, key=category_averages.get)
                else:
                    best_category = "None"
                
                return DashboardStats(
                    total_attempts=total_attempts,
                    average_score=round(average_score, 2),
                    improvement_rate=round(improvement_rate, 2),
                    best_category=best_category,
                    attempts_by_category=attempts_by_category
                )
            except Exception as calc_error:
                logger.error(f"Error calculating statistics: {str(calc_error)}", exc_info=True)
                # Return partial stats instead of crashing
                return DashboardStats(
                    total_attempts=len(evaluations),
                    average_score=0.0,
                    improvement_rate=0.0,
                    best_category="None",
                    attempts_by_category={}
                )
        except Exception as e:
            logger.error(f"Error in get_dashboard_stats: {str(e)}", exc_info=True)
            # Don't re-raise if it's already a formatted error
            if "Authentication failed" in str(e):
                raise
            raise Exception(f"Failed to get dashboard stats: {str(e)}")
    
    async def get_progress_trends(self, user_token: str, days: int = 30) -> List[ProgressTrend]:
        """Get user's progress trends over time."""
        try:
            user = await self.auth_service.get_user(user_token)
            
            # Get evaluations from the last N days
            start_date = datetime.now() - timedelta(days=days)
            
            response = self.supabase.table("evaluations")\
                .select("*")\
                .eq("user_id", user.id)\
                .gte("created_at", start_date.isoformat())\
                .order("created_at", desc=False)\
                .execute()
            
            evaluations = response.data
            
            # Group by date
            trends_by_date = {}
            for eval in evaluations:
                eval_date = datetime.fromisoformat(eval["created_at"]).date()
                date_str = eval_date.isoformat()
                
                if date_str not in trends_by_date:
                    trends_by_date[date_str] = {
                        "scores": [],
                        "attempts": 0
                    }
                
                trends_by_date[date_str]["scores"].append(eval["overall_score"])
                trends_by_date[date_str]["attempts"] += 1
            
            # Convert to list of ProgressTrend objects
            trends = []
            for date_str, data in sorted(trends_by_date.items()):
                avg_score = sum(data["scores"]) / len(data["scores"])
                trends.append(ProgressTrend(
                    date=date_str,
                    average_score=round(avg_score, 2),
                    attempts=data["attempts"]
                ))
            
            return trends
        except Exception as e:
            raise Exception(f"Failed to get progress trends: {str(e)}")
    
    async def get_top_mistakes(self, user_token: str) -> List[TopMistake]:
        """Get user's top 3 most common mistakes."""
        try:
            user = await self.auth_service.get_user(user_token)
            
            # Get all evaluations
            response = self.supabase.table("evaluations")\
                .select("*")\
                .eq("user_id", user.id)\
                .execute()
            
            evaluations = response.data
            
            # Collect all suggestions
            all_suggestions = []
            for eval in evaluations:
                if "suggestions" in eval and eval["suggestions"]:
                    all_suggestions.extend(eval["suggestions"])
            
            # Count by category
            category_counter = Counter(s["category"] for s in all_suggestions)
            
            # Get top 3
            top_3 = category_counter.most_common(3)
            
            # Create TopMistake objects with descriptions
            mistake_descriptions = {
                "clarity": "Prompts lack clear structure and organization",
                "specificity": "Instructions are too vague or general",
                "creativity": "Prompts could be more unique and innovative",
                "relevance": "Prompts don't fully align with challenge goals",
                "general": "General improvements needed in prompt construction"
            }
            
            mistakes = []
            for category, frequency in top_3:
                mistakes.append(TopMistake(
                    category=category,
                    frequency=frequency,
                    description=mistake_descriptions.get(category, "Area for improvement")
                ))
            
            return mistakes
        except Exception as e:
            raise Exception(f"Failed to get top mistakes: {str(e)}")
    
    async def get_category_stats(self, user_token: str, category: str) -> dict:
        """Get statistics for a specific category."""
        try:
            user = await self.auth_service.get_user(user_token)
            
            # Get challenges in this category
            challenges_response = self.supabase.table("challenges")\
                .select("id")\
                .eq("category", category)\
                .execute()
            
            challenge_ids = [c["id"] for c in challenges_response.data]
            
            if not challenge_ids:
                return {
                    "category": category,
                    "total_attempts": 0,
                    "average_score": 0.0,
                    "best_score": 0.0,
                    "recent_trend": "no_data"
                }
            
            # Get evaluations for these challenges
            evaluations = []
            for challenge_id in challenge_ids:
                response = self.supabase.table("evaluations")\
                    .select("*")\
                    .eq("user_id", user.id)\
                    .eq("challenge_id", challenge_id)\
                    .order("created_at", desc=False)\
                    .execute()
                evaluations.extend(response.data)
            
            if not evaluations:
                return {
                    "category": category,
                    "total_attempts": 0,
                    "average_score": 0.0,
                    "best_score": 0.0,
                    "recent_trend": "no_data"
                }
            
            total_attempts = len(evaluations)
            scores = [e["overall_score"] for e in evaluations]
            average_score = sum(scores) / total_attempts
            best_score = max(scores)
            
            # Calculate recent trend
            if total_attempts >= 3:
                recent_avg = sum(scores[-3:]) / 3
                older_avg = sum(scores[:-3]) / (total_attempts - 3) if total_attempts > 3 else average_score
                
                if recent_avg > older_avg * 1.1:
                    recent_trend = "improving"
                elif recent_avg < older_avg * 0.9:
                    recent_trend = "declining"
                else:
                    recent_trend = "stable"
            else:
                recent_trend = "insufficient_data"
            
            return {
                "category": category,
                "total_attempts": total_attempts,
                "average_score": round(average_score, 2),
                "best_score": round(best_score, 2),
                "recent_trend": recent_trend
            }
        except Exception as e:
            raise Exception(f"Failed to get category stats: {str(e)}")
