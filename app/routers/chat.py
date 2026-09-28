from fastapi import APIRouter, Depends, HTTPException

from app.auth.dependencies import get_current_user
from app.schemas import ChatRequest, ChatResponse
from app.services.cache_service import CacheService
from app.services.chat_service import ChatService
from app.services.llm_service import LLMService
from app.services.rag_service import RAGService


router = APIRouter(
    prefix="/api/v1/chat",
    tags=["Chat"],
)


rag_service = RAGService()
llm_service = LLMService()
cache_service = CacheService()

chat_service = ChatService(
    rag_service=rag_service,
    llm_service=llm_service,
    cache_service=cache_service,
)


@router.post(
    "",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
    current_user: dict = Depends(get_current_user),
):

    try:

        result = await chat_service.chat(
            query=request.query,
            user_id=current_user["user_id"],
            tenant_id=current_user["tenant_id"],
        )

        return result

    except RuntimeError as exc:

        raise HTTPException(
            status_code=503,
            detail=str(exc),
        )
