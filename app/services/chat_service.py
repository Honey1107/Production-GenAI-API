from app.services.cache_service import CacheService
from app.services.llm_service import LLMService
from app.services.rag_service import RAGService


class ChatService:

    def __init__(
        self,
        rag_service: RAGService,
        llm_service: LLMService,
        cache_service: CacheService,
    ):

        self.rag_service = rag_service
        self.llm_service = llm_service
        self.cache_service = cache_service

    async def chat(
        self,
        query: str,
        user_id: str,
        tenant_id: str,
    ) -> dict:

        # 1. Check cache
        cached_answer = self.cache_service.get(query)

        if cached_answer is not None:

            return {
                "answer": cached_answer,
                "cached": True,
                "sources": [],
            }

        # 2. Retrieve authorized context
        documents = await self.rag_service.retrieve(
            query=query,
            user_id=user_id,
            tenant_id=tenant_id,
        )

        # 3. Build context
        context = "\n\n".join(
            document["content"]
            for document in documents
        )

        # 4. Generate response
        answer = await self.llm_service.generate(
            query=query,
            context=context,
        )

        # 5. Cache response
        self.cache_service.set(
            query,
            answer,
        )

        return {
            "answer": answer,
            "cached": False,
            "sources": [
                document["name"]
                for document in documents
            ],
        }
