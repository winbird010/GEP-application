#!/user/bin/env python3
# -*- coding: utf-8 -*-

# app/core/cache.py
import redis.asyncio as redis
from contextlib import asynccontextmanager
from app.core.config import settings

# 不再全局单例
async def get_redis():
    """每次依赖注入都新建连接，测试结束自动关闭。"""
    async with redis.from_url(settings.REDIS_URL, decode_responses=True) as conn:
        yield conn

# 向后兼容：全局单例（不依赖注入时仍可用）
redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)