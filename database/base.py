# database/base.py

from typing import AsyncGenerator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Database:
    def __init__(self, database_url: str):
        self.database_url = f"sqlite+aiosqlite:///{database_url}"
        self.engine = create_async_engine(
            self.database_url,
            echo=True
        )
        self.session_maker = sessionmaker(
            self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def create_db_and_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_maker() as session:
            yield session