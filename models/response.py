from pydantic import BaseModel
from models.member import MemberResponse
from typing import Any


class ResultBase(BaseModel):
    code: str = "000000"
    message: str = "success"

    class Config:
        json_schema_extra = {"example": {"code": "000000", "message": "success"}}


class ResponseBase(BaseModel):
    result: ResultBase
    data: MemberResponse | Any  # | add others...
