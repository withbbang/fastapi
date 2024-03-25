from pydantic import BaseModel


# 관리자 계정 모델
class AdminBase(BaseModel):
    memberFK: str
    memberId: str
    password: str
    grade: int = 50

    # TODO: Config - 예시 파라미터
    class Config:
        json_schema_extra = {"example": {"id": 0, "name": "상남자"}}


class AdminResponse(AdminBase):
    id: str

    class Config:
        orm_mode = True
