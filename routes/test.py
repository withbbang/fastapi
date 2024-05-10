import asyncio
from fastapi import APIRouter
from models import ResultBase, ResponseBase
from services import raise_add_test, add_test
from database import session
from utils import Result
from depends import session
from decoraters import Transactional

test_router = APIRouter(tags=["Test"])


@test_router.post("/", response_model=ResponseBase)
@Transactional()
async def test(session: session):
    # await asyncio.gather(raise_add_test(session), add_test(session))

    await add_test(session)
    await raise_add_test(session)

    result = ResultBase()
    result.setResult(**Result.WARNING.value)
    response = ResponseBase(result=result, data=None)

    return response


@test_router.get("/", response_model=ResponseBase)
def test():
    result = ResultBase()
    result.setResult(**Result.INFO.value)
    response = ResponseBase(result=result, data=None)

    return response
