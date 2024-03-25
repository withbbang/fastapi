from pydantic import BaseModel
from datetime import date, datetime


# 기수 모델
class DegreenBase(BaseModel):
    degree: str
    color: str

    # TODO: Config - 예시 파라미터
    class Config:
        json_schema_extra = {"example": {"id": 0, "name": "상남자"}}


class DegreenResponse(DegreenBase):
    id: str

    class Config:
        orm_mode = True
