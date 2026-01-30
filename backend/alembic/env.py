# alembic/env.py
import asyncio
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from sqlalchemy.engine import Connection
# 移除：from sqlalchemy.ext.asyncio import AsyncEngine

from alembic import context

# 导入模型基类
from app.db.base import Base
from app.models.content import Content  # 确保导入所有模型

# this is the Alembic Config object
config = context.config

# 解释配置文件中的 Python 日志设置
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 元数据目标
target_metadata = Base.metadata


# 关键修改：使用同步 URL（去掉 +aiosqlite）
# 在 alembic.ini 中配置同步 URL，或在这里覆盖
def get_url():
    # 同步 SQLite URL
    return "sqlite:///./gep.db"


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