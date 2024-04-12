from fastapi import APIRouter
from models.response import ResultBase, ResponseBase
from services.test import raise_add_test, add_test
from database.connection import session
from utils.results import Result

test_router = APIRouter(tags=["Test"])


@test_router.post("/", response_model=ResponseBase)
async def test():
    print("test router: ", session)
    result = ResultBase()
    result.setResult(**Result.WARNING.value)

    import asyncio

    await asyncio.gather(raise_add_test(session), add_test(session))

    response = ResponseBase(result=result, data=None)

    return response
