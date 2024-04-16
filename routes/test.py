import asyncio
from fastapi import APIRouter
from models import ResultBase, ResponseBase
from services import raise_add_test, add_test
from database import session
from utils import Result


test_router = APIRouter(tags=["Test"])


@test_router.post("/", response_model=ResponseBase)
async def test():
    print("test router: ", session)
    result = ResultBase()
    result.setResult(**Result.WARNING.value)

    await asyncio.gather(raise_add_test(session), add_test(session))

    response = ResponseBase(result=result, data=None)

    return response
