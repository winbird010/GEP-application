#!/user/bin/env python3
# -*- coding: utf-8 -*-

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="GEP Platform API", version="1.0.0")
origins_str = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173")
origins = [origin.strip() for origin in origins_str.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 生产环境前端
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
@app.head("/api/health")
async def health_check():
    return {"status": "ok", "service": "gep-api", "version": "1.0.0"}


@app.get("/")
async def root():
    return {"message": "GEP API", "docs": "/docs", "health": "/api/health"}


from app.routers import content

app.include_router(content.router)

from app.routers import home

app.include_router(home.router)
