#!/user/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Index
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class Content(Base):
    __tablename__ = "contents"
    # 复合索引（顺序：slug 在前，is_active 在后）
    __table_args__ = (
        Index("ix_content_slug_active", "slug", "is_active"),
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    slug: Mapped[str] = mapped_column(unique=True, index=True)
    title: Mapped[str]
    subtitle: Mapped[str]
    content: Mapped[str]  # 存储完整HTML或Markdown
    icon: Mapped[str]
    sort_order: Mapped[int] = mapped_column(default=0)
    is_active: Mapped[bool] = mapped_column(default=True)
