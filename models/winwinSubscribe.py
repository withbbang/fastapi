from pydantic import BaseModel


# 상생 신청 모델
class WinwinSubscribeBase(BaseModel):
    memberFK: str
    comment: str = ""
    status: str = "W"  # W: 신청 대기 / R: 신청 거절 / A: 신청 수락

    # TODO: Config - 예시 파라미터
    class Config:
        json_schema_extra = {"example": {"id": 0, "name": "상남자"}}


class WinwinSubscribeResponse(WinwinSubscribeBase):
    id: str

    class Config:
        orm_mode = True
