import os
import contextlib
from fastapi import Depends
from dotenv import load_dotenv
from typing import Annotated, AsyncIterator
from contextvars import ContextVar, Token
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    async_scoped_session,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

Base = declarative_base()

session_context: ContextVar[str] = ContextVar("session_context")


def get_session_context() -> str:
    return session_context.get()


def set_session_context(session_id: str) -> Token:
    return session_context.set(session_id)


def reset_session_context(context: Token) -> None:
    session_context.reset(context)


class DatabaseSessionManager:
    def __init__(self, host: str):
        self._engine = create_async_engine(host, pool_recycle=3600, echo=True)
        # self._sessionmaker = async_sessionmaker(autocommit=False, bind=self._engine)
        self._sessionmaker = async_sessionmaker(
            autocommit=False, autoflush=False, bind=self._engine, class_=AsyncSession
        )
        self._session = async_scoped_session(
            session_factory=self._sessionmaker, scopefunc=get_session_context
        )

    async def close(self):
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")
        await self._engine.dispose()

        self._engine = None
        self._sessionmaker = None
        self._session = None

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")

        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._session is None:
            raise Exception("DatabaseSessionManager is not initialized")

        session = self._session()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


sessionmanager = DatabaseSessionManager(DATABASE_URL)


async def get_db_session():
    async with sessionmanager.session() as session:
        yield session
