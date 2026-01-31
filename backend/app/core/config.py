#!/user/bin/env python3
# -*- coding: utf-8 -*-
# backend/app/core/config.py
from pydantic_settings import BaseSettings  # 需要 pip install pydantic-settings


class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str

    # 给 SQLAlchemy 用的完整 URL（自动补 +asyncpg）
    @property
    def DATABASE_URL_ASYNC(self) -> str:
        return (
            self.DATABASE_URL
            if "+asyncpg" in self.DATABASE_URL
            else self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)
        )

    class Config:
        env_file = ".env"  # 本地用；Render 用环境变量覆盖


settings = Settings()
