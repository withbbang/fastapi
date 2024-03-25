from pydantic import BaseModel


# 벙 상태 모델
class MeetingStatusBase(BaseModel):
    status: int

    # TODO: Config - 예시 파라미터
    class Config:
        json_schema_extra = {"example": {"id": 0, "name": "상남자"}}


class MeetingStatusResponse(MeetingStatusBase):
    id: str

    class Config:
        orm_mode = True
