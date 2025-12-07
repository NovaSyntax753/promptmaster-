import httpx
import json
from supabase import create_client, Client
from app.core.config import settings
from app.models.schemas import (
    EvaluationResult, EvaluationScore, ImprovementSuggestion
)
from app.services.auth_service import AuthService
from app.services.challenge_service import ChallengeService
from typing import List, Optional
from datetime import datetime


class EvaluationService:
    def __init__(self):
        self.supabase: Client = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_KEY
        )
        self.auth_service = AuthService()
        self.challenge_service = ChallengeService()
    
    async def evaluate_prompt(
        self,
        user_token: str,
        challenge_id: int,
        user_prompt: str
    ) -> EvaluationResult:
        """Evaluate a user's prompt and provide scores with suggestions."""
        try:
            # Get user
            user = await self.auth_service.get_user(user_token)
            
            # Get challenge
            challenge = await self.challenge_service.get_challenge_by_id(challenge_id)
            if not challenge:
                raise Exception("Challenge not found")
            
            # Generate AI output using user's prompt
            ai_output = await self._generate_ai_response(user_prompt, challenge.goal)
            
            # Evaluate the prompt
            scores = await self._evaluate_prompt_quality(
                user_prompt, challenge.goal, challenge.example_prompt
            )
            
            # Generate improvement suggestions
            suggestions = await self._generate_suggestions(
                user_prompt, challenge.goal, scores
            )
            
            # Store evaluation in database
            evaluation_data = {
                "user_id": user.id,
                "challenge_id": challenge_id,
                "user_prompt": user_prompt,
                "ai_output": ai_output,
                "clarity_score": scores.clarity,
                "specificity_score": scores.specificity,
                "creativity_score": scores.creativity,
                "relevance_score": scores.relevance,
                "overall_score": scores.overall,
                "suggestions": [s.dict() for s in suggestions]
            }
            
            response = self.supabase.table("evaluations")\
                .insert(evaluation_data)\
                .execute()
            
            return EvaluationResult(
                id=response.data[0]["id"],
                user_id=user.id,
                challenge_id=challenge_id,
                user_prompt=user_prompt,
                ai_output=ai_output,
                scores=scores,
                suggestions=suggestions,
                created_at=datetime.now()
            )
        except Exception as e:
            raise Exception(f"Evaluation failed: {str(e)}")
    
    async def _generate_ai_response(self, user_prompt: str, goal: str) -> str:
        """Generate AI response using Groq API."""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {settings.GROQ_API_KEY}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": settings.DEFAULT_MODEL,
                        "messages": [
                            {
                                "role": "system",
                                "content": f"You are helping with this task: {goal}"
                            },
                            {
                                "role": "user",
                                "content": user_prompt
                            }
                        ]
                    },
                    timeout=30.0
                )
                
                if response.status_code != 200:
                    error_text = response.text
                    print(f"[GROQ ERROR] Status {response.status_code}: {error_text}")
                    return f"Error generating response: API returned {response.status_code}"
                
                result = response.json()
                content = result["choices"][0]["message"]["content"]
                print(f"[GROQ SUCCESS] Generated AI response ({len(content)} chars)")
                return content
        except Exception as e:
            print(f"Exception in _generate_ai_response: {str(e)}")
            return f"Error generating response: {str(e)}"
    
    async def _evaluate_prompt_quality(
        self,
        user_prompt: str,
        goal: str,
        example_prompt: str
    ) -> EvaluationScore:
        """Evaluate prompt quality using strict 5-criteria rubric."""
        try:
            evaluation_prompt = f"""You are a strict and consistent Prompt Quality Evaluator. Your job is to rate the given prompt on a scale from 1 to 10 based on five criteria. You must think through each criterion step by step before giving a final score.

CHALLENGE GOAL: {goal}

EXAMPLE PROMPT: {example_prompt}

USER'S PROMPT TO EVALUATE: {user_prompt}

Evaluation Criteria (each worth 2 points):
1. Clarity – The prompt should be easy to understand in one reading. (0 = fails, 1 = partial, 2 = fully meets)
2. Purpose – The prompt should clearly state the goal or expected result. (0 = fails, 1 = partial, 2 = fully meets)
3. Structure – The prompt should have organized instructions, formatting, steps, or bullet points when needed. (0 = fails, 1 = partial, 2 = fully meets)
4. Completeness – The prompt should include enough detail for a useful, high-quality response. (0 = fails, 1 = partial, 2 = fully meets)
5. Language Quality – The prompt should be readable, grammatically correct, and free of confusing wording. (0 = fails, 1 = partial, 2 = fully meets)

Think through each criterion step by step, then respond with ONLY valid JSON in this exact format:
{{
    "clarity": 2,
    "purpose": 1,
    "structure": 2,
    "completeness": 1,
    "language_quality": 2,
    "reasoning": {{
        "clarity": "Brief explanation of clarity score",
        "purpose": "Brief explanation of purpose score",
        "structure": "Brief explanation of structure score",
        "completeness": "Brief explanation of completeness score",
        "language_quality": "Brief explanation of language quality score"
    }}
}}

Scores must be integers: 0, 1, or 2 only."""

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {settings.GROQ_API_KEY}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": settings.EVALUATION_MODEL,
                        "messages": [
                            {
                                "role": "user",
                                "content": evaluation_prompt
                            }
                        ],
                        "temperature": 0.3
                    },
                    timeout=30.0
                )
                
                if response.status_code != 200:
                    error_text = response.text
                    error_msg = f"Groq API returned {response.status_code}: {error_text}"
                    print(f"[GROQ ERROR - EVALUATION] {error_msg}")
                    raise Exception(error_msg)
                
                result = response.json()
                scores_text = result["choices"][0]["message"]["content"]
                
                print(f"[GROQ RAW EVALUATION]:\n{scores_text}")
                
                # Extract JSON from response
                try:
                    scores_json = json.loads(scores_text)
                except json.JSONDecodeError as je:
                    print(f"[JSON PARSE ERROR] Could not parse: {scores_text}")
                    raise Exception(f"Invalid JSON from Groq: {str(je)}")
                
                # Validate all required keys exist
                required_keys = ["clarity", "purpose", "structure", "completeness", "language_quality"]
                missing_keys = [k for k in required_keys if k not in scores_json]
                if missing_keys:
                    raise Exception(f"Missing keys in Groq response: {missing_keys}")
                
                # Calculate overall score (sum of all criteria, max 10)
                overall = (
                    scores_json["clarity"] + 
                    scores_json["purpose"] + 
                    scores_json["structure"] + 
                    scores_json["completeness"] + 
                    scores_json["language_quality"]
                )
                
                print(f"[SCORES] Clarity:{scores_json['clarity']} Purpose:{scores_json['purpose']} Structure:{scores_json['structure']} Completeness:{scores_json['completeness']} Language:{scores_json['language_quality']} | Total:{overall}/10")
                
                # Map to 0-10 scale for storage (keeping backward compatibility)
                return EvaluationScore(
                    clarity=scores_json["clarity"] * 5.0,  # 0-2 -> 0-10
                    specificity=scores_json["completeness"] * 5.0,
                    creativity=scores_json["structure"] * 5.0,
                    relevance=scores_json["purpose"] * 5.0,
                    overall=float(overall)  # Keep 0-10 scale
                )
        except Exception as e:
            print(f"[EVALUATION ERROR] Exception in _evaluate_prompt_quality: {str(e)}")
            import traceback
            traceback.print_exc()
            # Re-raise to surface the actual error instead of hiding it
            raise Exception(f"Prompt evaluation failed: {str(e)}")
    
    async def _generate_suggestions(
        self,
        user_prompt: str,
        goal: str,
        scores: EvaluationScore
    ) -> List[ImprovementSuggestion]:
        """Generate specific improvement suggestions based on 5-criteria evaluation."""
        try:
            # Convert scores back to 0-2 scale for analysis
            clarity_raw = int(scores.clarity / 5.0)
            purpose_raw = int(scores.relevance / 5.0)
            structure_raw = int(scores.creativity / 5.0)
            completeness_raw = int(scores.specificity / 5.0)
            
            suggestion_prompt = f"""Based on the prompt evaluation, provide 3-5 specific improvement suggestions.

CHALLENGE GOAL: {goal}

USER'S PROMPT: {user_prompt}

EVALUATION SCORES (0-2 scale):
- Clarity: {clarity_raw}/2 (ease of understanding)
- Purpose: {purpose_raw}/2 (clear goal statement)
- Structure: {structure_raw}/2 (organized format)
- Completeness: {completeness_raw}/2 (sufficient detail)
- Language Quality: (grammar and readability)

Overall Score: {scores.overall}/10

Provide actionable suggestions to improve this prompt. Focus on the lowest-scoring criteria.

Respond ONLY with valid JSON in this exact format:
[
    {{
        "category": "clarity",
        "suggestion": "Break down your prompt into numbered steps for better structure",
        "priority": "high"
    }},
    {{
        "category": "purpose",
        "suggestion": "Clearly state what output format or result you expect",
        "priority": "medium"
    }}
]

Valid categories: clarity, purpose, structure, completeness, language, general
Valid priorities: high, medium, low"""

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {settings.GROQ_API_KEY}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": settings.EVALUATION_MODEL,
                        "messages": [
                            {
                                "role": "user",
                                "content": suggestion_prompt
                            }
                        ],
                        "temperature": 0.7
                    },
                    timeout=30.0
                )
                
                if response.status_code != 200:
                    error_text = response.text
                    print(f"[GROQ ERROR - SUGGESTIONS] Status {response.status_code}: {error_text}")
                    # Use generic suggestions as fallback (non-critical feature)
                    return [
                        ImprovementSuggestion(
                            category="general",
                            suggestion="Be more specific about the expected output format",
                            priority="medium"
                        ),
                        ImprovementSuggestion(
                            category="general",
                            suggestion="Add context about the target audience or use case",
                            priority="medium"
                        )
                    ]
                
                result = response.json()
                suggestions_text = result["choices"][0]["message"]["content"]
                
                print(f"[GROQ RAW SUGGESTIONS]:\n{suggestions_text}")
                
                # Extract JSON from response
                suggestions_json = json.loads(suggestions_text)
                
                return [ImprovementSuggestion(**s) for s in suggestions_json]
        except Exception as e:
            print(f"[SUGGESTIONS ERROR] Exception in _generate_suggestions: {str(e)}")
            import traceback
            traceback.print_exc()
            # Fallback to generic suggestions (non-critical feature)
            return [
                ImprovementSuggestion(
                    category="general",
                    suggestion="Be more specific about the expected output format",
                    priority="medium"
                ),
                ImprovementSuggestion(
                    category="general",
                    suggestion="Add context about the target audience or use case",
                    priority="medium"
                )
            ]
    
    async def get_user_history(
        self,
        user_token: str,
        limit: int = 10,
        offset: int = 0,
        challenge_id: Optional[int] = None
    ) -> List[EvaluationResult]:
        """Get user's evaluation history."""
        try:
            user = await self.auth_service.get_user(user_token)
            
            query = self.supabase.table("evaluations")\
                .select("*")\
                .eq("user_id", user.id)\
                .order("created_at", desc=True)\
                .limit(limit)\
                .offset(offset)
            
            if challenge_id:
                query = query.eq("challenge_id", challenge_id)
            
            response = query.execute()
            
            results = []
            for eval_data in response.data:
                results.append(EvaluationResult(
                    id=eval_data["id"],
                    user_id=eval_data["user_id"],
                    challenge_id=eval_data["challenge_id"],
                    user_prompt=eval_data["user_prompt"],
                    ai_output=eval_data["ai_output"],
                    scores=EvaluationScore(
                        clarity=eval_data["clarity_score"],
                        specificity=eval_data["specificity_score"],
                        creativity=eval_data["creativity_score"],
                        relevance=eval_data["relevance_score"],
                        overall=eval_data["overall_score"]
                    ),
                    suggestions=[
                        ImprovementSuggestion(**s) for s in eval_data["suggestions"]
                    ],
                    created_at=datetime.fromisoformat(eval_data["created_at"])
                ))
            
            return results
        except Exception as e:
            raise Exception(f"Failed to fetch history: {str(e)}")
    
    async def get_evaluation_by_id(
        self,
        evaluation_id: int,
        user_token: str
    ) -> Optional[EvaluationResult]:
        """Get a specific evaluation by ID."""
        try:
            user = await self.auth_service.get_user(user_token)
            
            response = self.supabase.table("evaluations")\
                .select("*")\
                .eq("id", evaluation_id)\
                .eq("user_id", user.id)\
                .execute()
            
            if not response.data:
                return None
            
            eval_data = response.data[0]
            
            return EvaluationResult(
                id=eval_data["id"],
                user_id=eval_data["user_id"],
                challenge_id=eval_data["challenge_id"],
                user_prompt=eval_data["user_prompt"],
                ai_output=eval_data["ai_output"],
                scores=EvaluationScore(
                    clarity=eval_data["clarity_score"],
                    specificity=eval_data["specificity_score"],
                    creativity=eval_data["creativity_score"],
                    relevance=eval_data["relevance_score"],
                    overall=eval_data["overall_score"]
                ),
                suggestions=[
                    ImprovementSuggestion(**s) for s in eval_data["suggestions"]
                ],
                created_at=datetime.fromisoformat(eval_data["created_at"])
            )
        except Exception as e:
            raise Exception(f"Failed to fetch evaluation: {str(e)}")
