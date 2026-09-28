from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ChatRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=1,
        max_length=5000,
    )


class ChatResponse(BaseModel):
    answer: str
    cached: bool
    sources: list[str]
