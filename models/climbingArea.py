from pydantic import BaseModel
from datetime import datetime


# 암장 모델
class ClimbingAreaBase(BaseModel):
    climbingAreaName: str
    price: str
    address: str
    winwinYn: str = "N"
    createDt: datetime
    updateDt: datetime | None = None

    # TODO: Config - 예시 파라미터
    class Config:
        json_schema_extra = {"example": {"id": 0, "name": "상남자"}}


class ClimbingAreaResponse(ClimbingAreaBase):
    id: str

    class Config:
        orm_mode = True
