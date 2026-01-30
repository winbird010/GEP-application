#!/user/bin/env python3
# -*- coding: utf-8 -*-

import pytest, asyncio
from playwright.async_api import async_playwright

BASE_URL = "http://localhost:5173"          # Vite 默认前端地址

@pytest.mark.asyncio
async def test_home_to_financing(page):
    """首页 → 融资信贷 → 内容渲染 → 返回"""
    await page.goto(BASE_URL)
    await page.click('text=融资信贷')
    await page.wait_for_selector('h1:has-text("融资信贷")')
    content = await page.text_content('.content-text')
    assert len(content) >= 100               # 字数阈值
    await page.click('text=GEP应用')          # 返回首页
    await page.wait_for_selector('text=GEP应用', state='visible')  # ✅ 宽松等待

@pytest.mark.asyncio
async def test_5_pages_data(browser):
    """5 条 slug 并行访问，总耗时 ≈ 最慢一次"""
    slugs = ["financing", "compensation", "trading", "damage", "others"]

    async def open_and_check(slug: str):
        page = await browser.new_page()
        try:
            await page.goto(f"{BASE_URL}/{slug}", wait_until="domcontentloaded")
            await page.wait_for_selector('.content-text', timeout=3000)
            txt = await page.text_content('.content-text')
            assert len(txt) > 50, f"{slug} 内容过短"
        finally:
            await page.close()

    # 同时启动 5 个协程
    await asyncio.gather(*(open_and_check(s) for s in slugs))