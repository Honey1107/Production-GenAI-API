DOCUMENTS = [
    {
        "id": "doc-1",
        "owner_id": "user-1",
        "tenant_id": "company-a",
        "name": "loan_policy.txt",
        "content": (
            "Personal loans require identity verification "
            "and credit assessment."
        ),
    },
    {
        "id": "doc-2",
        "owner_id": "user-1",
        "tenant_id": "company-a",
        "name": "account_policy.txt",
        "content": (
            "Customers can update account information "
            "after successful authentication."
        ),
    },
    {
        "id": "doc-3",
        "owner_id": "user-2",
        "tenant_id": "company-b",
        "name": "internal_policy.txt",
        "content": (
            "This document belongs to another tenant."
        ),
    },
]


class RAGService:

    async def retrieve(
        self,
        query: str,
        user_id: str,
        tenant_id: str,
    ) -> list[dict]:

        query_words = set(
            query.lower().split()
        )

        results = []

        for document in DOCUMENTS:

            # Security boundary
            if document["owner_id"] != user_id:
                continue

            if document["tenant_id"] != tenant_id:
                continue

            content_words = set(
                document["content"].lower().split()
            )

            if query_words & content_words:
                results.append(document)

        return results

