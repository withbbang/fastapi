from fastapi import APIRouter
from models import ResultBase, ResponseBase
from services import get_all_members, get_member
from utils import Result
from depends import session
import time

member_router = APIRouter(tags=["Member"])


@member_router.get("/test", response_model=ResponseBase)
async def read_all_members_(
    session: session,
):
    result = ResultBase()
    result.setResult(**Result.WARNING.value)
    data = await get_all_members(session)

    response = ResponseBase(result=result, data=data)

    return response


@member_router.get("/", response_model=ResponseBase)
async def read_all_members():
    result = ResultBase()
    result.setResult(**Result.WARNING.value)
    data = await get_all_members(session)

    response = ResponseBase(result=result, data=data)

    return response


@member_router.get("/0", response_model=ResponseBase)
async def read_member():
    """
    특정 멤버 읽기 API

    **Example**
    ```python
    from database.connection import get_db
    ...
    ```
    """
    result = ResultBase()
    result.setResult(**Result.ERROR.value)

    data = await get_member(session)

    # time.sleep(5) session registry stack을 확인하기 위한 sleep

    response = ResponseBase(result=result, data=data)

    return response
