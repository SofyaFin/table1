import os
from functools import lru_cache

from pydantic import ConfigDict, PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""
    # Проверь ссылку!
    DB_DSN: PostgresDsn = "postgresql://postgres:232323@localhost:5432/postgres"
    ROOT_PATH: str = "/" + os.getenv("APP_NAME", "")
    model_config = ConfigDict(case_sensitive=True, env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
