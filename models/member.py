from pydantic import BaseModel


class MemberBase(BaseModel):
    name: str
    birthDt: str
    levelFK: str
    degreeFK: str
    phoneNo: str | None = None
    winwinYn: str
    sex: str
    blackCnt: int
    dormancyYn: str
    leaveYn: str
    banYn: str
    joinDt: str
    createDt: str
    updateDt: str | None = None
    leaveDt: str | None = None
    banDt: str | None = None
    image: str | None = None
    updateReason: str | None = None
    dormancyReason: str | None = None
    leaveReason: str | None = None
    banReason: str | None = None

    # TODO: Config - 예시 파라미터
    class Config:
        json_schema_extra = {"example": {"id": 0, "name": "상남자"}}


class Member(MemberBase):
    id: str

    class Config:
        orm_mode = True
