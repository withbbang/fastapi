from pydantic import BaseModel
from datetime import date, datetime


# 상생 신청 모델
class WinwindSubscribeBase(BaseModel):
    memberFK: str
    comment: str

    # TODO: Config - 예시 파라미터
    class Config:
        json_schema_extra = {"example": {"id": 0, "name": "상남자"}}


class WinwindSubscribeResponse(WinwindSubscribeBase):
    id: str

    class Config:
        orm_mode = True
