#!/user/bin/env python3
# -*- coding: utf-8 -*-

# backend/app/schemas/content.py
from pydantic import BaseModel, ConfigDict  # ① 导入 ConfigDict


class ContentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # ② 替换旧 Config 类

    id: int
    slug: str
    title: str
    subtitle: str
    content: str
    icon: str
