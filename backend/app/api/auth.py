from fastapi import APIRouter, HTTPException, Depends
from app.models.schemas import UserCreate, Token, User
from app.services.auth_service import AuthService
from typing import Dict

router = APIRouter()
auth_service = AuthService()


@router.post("/signup", response_model=Token)
async def signup(user_data: UserCreate):
    """
    Register a new user with email and password.
    """
    try:
        result = await auth_service.sign_up(user_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=Token)
async def login(email: str, password: str):
    """
    Login with email and password.
    """
    try:
        result = await auth_service.sign_in(email, password)
        return result
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.post("/google")
async def google_auth():
    """
    Initiate Google OAuth login.
    """
    try:
        auth_url = await auth_service.google_sign_in()
        return {"url": auth_url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/me", response_model=User)
async def get_current_user(token: str):
    """
    Get current authenticated user information.
    """
    try:
        user = await auth_service.get_user(token)
        return user
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.post("/logout")
async def logout(token: str):
    """
    Logout current user.
    """
    try:
        await auth_service.sign_out(token)
        return {"message": "Successfully logged out"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
