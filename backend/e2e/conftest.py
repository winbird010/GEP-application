#!/user/bin/env python3
# -*- coding: utf-8 -*-

import pytest_asyncio          # 必须用桥接库
from playwright.async_api import async_playwright

@pytest_asyncio.fixture
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        yield browser
        await browser.close()

@pytest_asyncio.fixture
async def page(browser):
    context = await browser.new_context()
    page_obj = await context.new_page()
    yield page_obj
    await context.close()