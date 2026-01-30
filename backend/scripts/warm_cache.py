#!/user/bin/env python3
# -*- coding: utf-8 -*-

import asyncio, json
from app.core.cache import redis_client
from sqlalchemy import select          # 新增
from app.models.content import Content
from app.db.session import async_session_maker

async def warm():
    async with async_session_maker() as db:
        rows = await db.scalars(
            select(Content).where(Content.is_active == True)   # 现在不再报错
        )
        for c in rows:
            key = f"content:{c.slug}"
            await redis_client.setex(key, 900, json.dumps({
                "id": c.id, "slug": c.slug, "title": c.title,
                "subtitle": c.subtitle, "content": c.content, "icon": c.icon
            }))

if __name__ == "__main__":
    asyncio.run(warm())
