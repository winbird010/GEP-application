#!/user/bin/env python3
# -*- coding: utf-8 -*-

import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import pytest
from httpx import AsyncClient
from app.main import app
from httpx._transports.asgi import ASGITransport   # 新增

# tests/test_api.py 内每个异步测试函数
@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/api/health")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_content():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/api/contents/financing")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_home():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/api/home/")
    assert response.status_code == 200