import os
from fastapi import APIRouter
from config import cursor

test_router = APIRouter()


@test_router.get("/")
async def test() -> dict:
    cursor.execute("SELECT * FROM MEMBER")

    print(cursor.fetchall())

    return {"response": "HELLO"}
