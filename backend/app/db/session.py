#!/user/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.pool import NullPool
from app.db.base import Base

DATABASE_URL = "sqlite+aiosqlite:///./gep.db"

engine = create_async_engine(
    DATABASE_URL,
    echo=False,               # 生产关闭日志
    poolclass=NullPool,         # ← 关键：SQLite 只能用它
    # pool_size=20,             # 同步池大小
    # max_overflow=40,          # 额外连接
    pool_pre_ping=True,       # 连接健康检查
)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
