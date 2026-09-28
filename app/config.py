from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    groq_api_key: str
    jwt_secret_key: str
    llm_model: str = "llama-3.3-70b-versatile"
    llm_temperature: float = 0.2
    llm_max_tokens: int = 1024
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 30
    cache_ttl_seconds: int = 60

settings = Settings()