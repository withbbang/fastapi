from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.member import MemberResponse
from models.response import ResultBase, ResponseBase
from queries.member import get_all_members, get_member
from database.connection import get_db
from utils.results import Result

member_router = APIRouter(tags=["Member"])


@member_router.get("/", response_model=ResponseBase)
def read_all_members(db: Session = Depends(get_db)):
    result = ResultBase()
    result.setResult(**Result.WARNING.value)
    data = get_all_members(db)

    response = ResponseBase(result=result, data=data)

    return response


@member_router.get("/0", response_model=ResponseBase)
def read_member(db: Session = Depends(get_db)):
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
    data = get_member(db)

    response = ResponseBase(result=result, data=data)

    return response
