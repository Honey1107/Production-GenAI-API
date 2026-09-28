from fastapi import APIRouter, HTTPException

from app.auth.security import (
    create_access_token,
    verify_password,
)
from app.schemas import LoginRequest, TokenResponse


router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"],
)


users = {
    "user1": {
        "user_id": "user-1",
        "tenant_id": "company-a",
        "password": "password123",
    },
    "user2": {
        "user_id": "user-2",
        "tenant_id": "company-b",
        "password": "password456",
    },
}


@router.post(
    "/login",
    response_model=TokenResponse,
)
async def login(request: LoginRequest):

    user = users.get(request.username)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    if request.password != user["password"]:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    token = create_access_token(
        user_id=user["user_id"],
        tenant_id=user["tenant_id"],
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }
