import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./data/social_poster.db"
    REDIS_URL: str = "redis://redis:6379/0"
    SESSION_DIR: str = "./data/sessions"
    MEDIA_DIR: str = "./data/media"

    class Config:
        env_file = ".env"

settings = Settings()

# Ensure directories exist
os.makedirs(settings.SESSION_DIR, exist_ok=True)
os.makedirs(settings.MEDIA_DIR, exist_ok=True)
