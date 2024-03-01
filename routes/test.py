import os
from fastapi import APIRouter
from dotenv import load_dotenv

load_dotenv()  # 환경변수 전체 load

SECRET_ENV = os.getenv("SECRET_ENV")  # 개별 환경변수 가져오기

test_router = APIRouter()


@test_router.get("/")
async def test() -> dict:
    return {"response": SECRET_ENV}
