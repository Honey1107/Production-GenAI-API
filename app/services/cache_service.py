import time

from app.config import settings  # Updated: Import the unified settings object


class CacheService:

    def __init__(self):
        self.cache: dict[str, tuple[float, str]] = {}

    def _normalize(self, query: str) -> str:
        return " ".join(
            query.lower().strip().split()
        )

    def get(
        self,
        query: str,
    ) -> str | None:

        key = self._normalize(query)

        item = self.cache.get(key)

        if not item:
            return None

        created_at, value = item

        # Updated: Access cache_ttl_seconds property from the settings object
        if time.time() - created_at > settings.cache_ttl_seconds:
            del self.cache[key]
            return None

        return value

    def set(
        self,
        query: str,
        answer: str,
    ) -> None:

        key = self._normalize(query)

        self.cache[key] = (
            time.time(),
            answer,
        )