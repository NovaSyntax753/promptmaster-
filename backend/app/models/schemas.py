from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: str
    created_at: datetime


class Token(BaseModel):
    access_token: str
    token_type: str
    user: User


class Challenge(BaseModel):
    id: int
    category: str
    title: str
    description: str
    goal: str
    example_prompt: str
    difficulty: str
    created_at: datetime


class PromptSubmission(BaseModel):
    challenge_id: int
    user_prompt: str


class EvaluationScore(BaseModel):
    clarity: float
    specificity: float
    creativity: float
    relevance: float
    overall: float


class ImprovementSuggestion(BaseModel):
    category: str
    suggestion: str
    priority: str


class EvaluationResult(BaseModel):
    id: int
    user_id: str
    challenge_id: int
    user_prompt: str
    ai_output: str
    scores: EvaluationScore
    suggestions: List[ImprovementSuggestion]
    created_at: datetime


class DashboardStats(BaseModel):
    total_attempts: int
    average_score: float
    improvement_rate: float
    best_category: str
    attempts_by_category: dict


class ProgressTrend(BaseModel):
    date: str
    average_score: float
    attempts: int


class TopMistake(BaseModel):
    category: str
    frequency: int
    description: str
