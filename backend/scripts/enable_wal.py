#!/user/bin/env python3
# -*- coding: utf-8 -*-

import aiosqlite, asyncio
async def wal():
    async with aiosqlite.connect("gep.db") as db:
        await db.execute("PRAGMA journal_mode=WAL;")
        await db.execute("PRAGMA synchronous=NORMAL;")
asyncio.run(wal())
