from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings.
    
    Environment variables will be loaded from .env file
    """
    
    # API settings
    APP_NAME: str = "api-template"
    API_VERSION: str = "v1"
    DEBUG: bool = Field(default=False)
    
    # Logging settings
    LOG_LEVEL: str = Field(default="INFO")
    
    # Database settings
    DATABASE_URL: Optional[str] = None
    
    # AWS settings
    AWS_REGION: str = Field(default="us-east-1")
    BUCKET_NAME: Optional[str] = None
    
    # Local development
    LOCAL_RUN: bool = Field(default=True)
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Get application settings from environment variables.
    Uses LRU cache to avoid reloading settings for each request.
    """
    return Settings() 