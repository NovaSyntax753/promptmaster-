from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    # Project Info
    PROJECT_NAME: str = "PromptMaster"
    API_V1_STR: str = "/api"
    ENVIRONMENT: str = "development"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        # Local development
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
        "http://localhost:5176",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
        "http://127.0.0.1:5175",
        "http://127.0.0.1:5176",
        # Production - Add your Vercel URL here after deployment
        "https://promptmaster-5f2t9k85k-tejas-dhoks-projects.vercel.app",  # Replace with your actual Vercel URL
        "https://promptmaster-six.vercel.app",  # Allow all Vercel preview deployments
    ]
    
    # Supabase
    SUPABASE_URL: str
    SUPABASE_KEY: str
    SUPABASE_JWT_SECRET: str
    
    # Database
    DATABASE_URL: str
    
    # AI API
    GROQ_API_KEY: str = ""
    OPENROUTER_API_KEY: str = ""
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    HUGGINGFACE_API_KEY: str = ""
    
    # AI Model Settings
    DEFAULT_MODEL: str = "llama-3.1-8b-instant"
    EVALUATION_MODEL: str = "llama-3.1-8b-instant"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
