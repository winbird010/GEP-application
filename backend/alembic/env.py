# alembic/env.py
import asyncio
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlalchemy.engine import Connection
from alembic import context

# 导入模型基类
from app.db.base import Base
from app.models.content import Content  # 确保导入所有模型
from app.core.config import settings

# this is the Alembic Config object
config = context.config

# 解释配置文件中的 Python 日志设置
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 元数据目标
target_metadata = Base.metadata


def get_url():
    """
    获取数据库 URL 并转换为 Alembic 可用的同步格式
    """
    url = settings.DATABASE_URL

    # 关键修改：Alembic 需要同步驱动，将异步驱动标识替换为同步的
    if "+asyncpg" in url:
        # 将 +asyncpg 替换为 +psycopg2（明确指定同步驱动）
        url = url.replace("+asyncpg", "+psycopg2")
    elif "+aiosqlite" in url:
        # 如果是 SQLite，去掉 +aiosqlite（SQLite 不区分同步异步）
        url = url.replace("+aiosqlite", "")

    return url


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    # 使用同步引擎
    configuration = config.get_section(config.config_ini_section)

    # 关键修改：取消注释并确保使用转换后的同步 URL
    configuration["sqlalchemy.url"] = get_url()

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        do_run_migrations(connection)


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()