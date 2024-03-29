from pydantic import BaseModel


class ResultBase(BaseModel):
    code: str
    message: str

    class Config:
        json_schema_extra = {"example": {"code": "000000", "message": "success"}}


class ResponseBase(BaseModel):
    result: ResultBase
    data: any
