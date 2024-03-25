from pydantic import BaseModel
from datetime import date, datetime


# 회원 레벨 모델
class LevelBase(BaseModel):
    level: str
    color: str

    # TODO: Config - 예시 파라미터
    class Config:
        json_schema_extra = {"example": {"id": 0, "name": "상남자"}}


class LevelResponse(LevelBase):
    id: str

    class Config:
        from_attributes = True
