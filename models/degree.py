from pydantic import BaseModel
from datetime import date, datetime


# 기수 모델
class DegreeBase(BaseModel):
    degree: str
    description: str

    # TODO: Config - 예시 파라미터
    class Config:
        json_schema_extra = {"example": {"id": 0, "name": "상남자"}}


class DegreeResponse(DegreeBase):
    id: str

    class Config:
        orm_mode = True
