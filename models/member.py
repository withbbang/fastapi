from pydantic import BaseModel
from datetime import date, datetime


# 회원 모델
class MemberBase(BaseModel):
    name: str
    birthDt: date
    levelFK: str
    degreeFK: str
    phoneNo: str | None = None
    winwinYn: str
    sex: str
    blackCnt: int
    dormancyYn: str
    leaveYn: str
    banYn: str
    joinDt: date
    createDt: datetime
    updateDt: datetime | None = None
    leaveDt: date | None = None
    banDt: datetime | None = None
    image: str | None = None
    updateReason: str | None = None
    dormancyReason: str | None = None
    leaveReason: str | None = None
    banReason: str | None = None

    # TODO: Config - 예시 파라미터
    class Config:
        json_schema_extra = {"example": {"id": 0, "name": "상남자"}}


class MemberResponse(MemberBase):
    id: str

    class Config:
        orm_mode = True
