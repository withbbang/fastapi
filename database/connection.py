# import os
# from contextlib import asynccontextmanager
# from dotenv import load_dotenv
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase, Session
# from contextvars import ContextVar, Token
# from typing import AsyncGenerator
# from sqlalchemy.ext.asyncio import (
#     AsyncSession,
#     create_async_engine,
#     async_sessionmaker,
#     async_scoped_session,
# )

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")

# session_context: ContextVar[str] = ContextVar("session_context")


# def get_session_context() -> str:
#     return session_context.get()


# def set_session_context(session_id: str) -> Token:
#     return session_context.set(session_id)


# def reset_session_context(context: Token) -> None:
#     session_context.reset(context)


# engine = create_async_engine(
#     DATABASE_URL,
#     pool_recycle=3600,
# )

# _async_session_factory = async_sessionmaker(
#     class_=AsyncSession,
#     sync_session_class=engine.sync_engine,
#     expire_on_commit=False,
# )
# session = async_scoped_session(
#     session_factory=_async_session_factory,
#     scopefunc=get_session_context,
# )


# class Base(DeclarativeBase): ...


# @asynccontextmanager
# async def session_factory() -> AsyncGenerator[AsyncSession, None]:
#     _session = async_sessionmaker(
#         class_=AsyncSession,
#         sync_session_class=engine.sync_engine,
#         expire_on_commit=False,
#     )()
#     try:
#         yield _session
#     finally:
#         await _session.close()


# 이전 코드
# sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from contextvars import ContextVar, Token

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

session_context: ContextVar[str] = ContextVar("session_context")


def get_session_context() -> str:
    return session_context.get()


def set_session_context(session_id: str) -> Token:
    return session_context.set(session_id)


def reset_session_context(context: Token) -> None:
    session_context.reset(context)


engine = create_async_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)  # 비동기 세션 생성
session = scoped_session(SessionLocal, scopefunc=get_session_context)

Base = declarative_base()
