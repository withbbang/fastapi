from pydantic import BaseModel


# 참석 모델
class AttendBase(BaseModel):
    memberFK: str
    memberFK: str

    # TODO: Config - 예시 파라미터
    class Config:
        json_schema_extra = {"example": {"id": 0, "name": "상남자"}}


class AttendResponse(AttendBase):
    id: str

    class Config:
        from_attributes = True
