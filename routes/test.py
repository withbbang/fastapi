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
    result = ResultBase()
    result.setResult(**Result.WARNING.value)

    await asyncio.gather(raise_add_test(session), add_test(session))

    response = ResponseBase(result=result, data=None)

    return response
