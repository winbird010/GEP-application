#!/user/bin/env python3
# -*- coding: utf-8 -*-

# app/routers/content.py
from fastapi import APIRouter, Depends, HTTPException, Response   # ← 1. 新增 Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.core.cache import redis_client
from app.models.content import Content
from app.schemas.content import ContentResponse
import json
from sqlalchemy import select
from app.core.cache import get_redis  # ① 引入新的依赖工厂

router = APIRouter(prefix="/api/contents", tags=["contents"])


@router.get("/{slug}", response_model=ContentResponse)
async def get_content(
    slug: str,
    response: Response,                          # ← 2. 注入 Response
    db: AsyncSession = Depends(get_db),
):
    """带 HTTP 缓存头的内容接口"""
    # ----- 缓存&业务逻辑（你已有） -----
    cache_key = f"content:{slug}"
    cached = await redis_client.get(cache_key)
    if cached:
        return json.loads(cached)

    row = await db.scalar(select(Content).where(Content.slug == slug))
    if not row:
        raise HTTPException(status_code=404, detail="Content not found")

    data = ContentResponse.model_validate(row).model_dump()
    await redis_client.setex(cache_key, 600, json.dumps(data))
    # -----------------------------------

    response.headers["Cache-Control"] = "public, max-age=600"  # ← 3. 加缓存头
    return data


@router.get("/", response_model=list[ContentResponse])
async def list_contents(
        db: AsyncSession = Depends(get_db),
        redis=Depends(get_redis)  # 同样注入，可选缓存
):
    # 简单示例：不做列表缓存，直接查库
    result = await db.execute(
        select(Content).where(Content.is_active == True).order_by(Content.sort_order)
    )
    return result.scalars().all()
