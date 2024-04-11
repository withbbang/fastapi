from fastapi import APIRouter
from models.response import ResultBase, ResponseBase
from services.member import get_all_members, get_member
from database.connection import session
from utils.results import Result
import time

member_router = APIRouter(tags=["Member"])


@member_router.get("/", response_model=ResponseBase)
def read_all_members():
    result = ResultBase()
    result.setResult(**Result.WARNING.value)
    data = get_all_members(session)

    response = ResponseBase(result=result, data=data)

    return response


@member_router.get("/0", response_model=ResponseBase)
def read_member():
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

    data = get_member(session)

    print(f"[*] registry: {session.registry.registry}")
    key = session.registry.scopefunc()
    print(f"[*] key: {key}")
    print(f"[*] session: {session.registry.registry[key]}")

    # time.sleep(5) session registry stack을 확인하기 위한 sleep

    response = ResponseBase(result=result, data=data)

    return response
