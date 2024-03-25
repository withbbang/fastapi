from pydantic import BaseModel
from datetime import datetime


# 벙 모델
class MeetingBase(BaseModel):
    name: str
    memberFK: str
    climbingAreaFK: str
    createDt: datetime
    hostDt: datetime
    updateDt: datetime
    deleteDt: datetime
    criticalMeetingYn: str
    meetingStatusFK: str

    # TODO: Config - 예시 파라미터
    class Config:
        json_schema_extra = {"example": {"id": 0, "name": "상남자"}}


class MeetingResponse(MeetingBase):
    id: str

    class Config:
        from_attributes = True
