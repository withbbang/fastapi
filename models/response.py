from pydantic import BaseModel
from models.member import MemberResponse
from typing import Any


class ResultBase(BaseModel):
    code: str
    message: str

    def __init__(self, code: str = "000000", message: str = "success"):
        super().__init__(code=code, message=message)

    def setResult(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    class Config:
        json_schema_extra = {"example": {"code": "000000", "message": "success"}}


class ResponseBase(BaseModel):
    result: ResultBase
    data: MemberResponse | Any  # | add others...
