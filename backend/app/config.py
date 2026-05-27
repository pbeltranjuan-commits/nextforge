from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://user:pass@localhost:5432/promptforge"
    ENCRYPTION_KEY: str = "32-char-base64-encryption-key-here=="
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "https://*.vercel.app"]
    DEFAULT_MODEL: str = "gpt-4-turbo"
    RATE_LIMIT_PER_MIN: int = 100

    class Config:
        env_file = ".env"

settings = Settings()
