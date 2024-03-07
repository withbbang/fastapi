import os
from fastapi import APIRouter
from typing import List
from config import cursor
from models.member import Member

test_router = APIRouter()


@test_router.get("/")
async def test() -> dict:
    cursor.execute("SELECT * FROM MEMBER")

    members = cursor.fetchall()

    return {"result": members}
