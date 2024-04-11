import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
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


engine = create_engine(DATABASE_URL)
con = engine.connect()
session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine),
    scopefunc=get_session_context,
)

Base = declarative_base()
