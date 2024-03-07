from datetime import datetime, time, timedelta
from pydantic import BaseModel


class Member(BaseModel):
    id: str
    name: str
    birthdt: str
    levelfk: int
    degreefk: int
    phoneno: str = None
    winwinyn: str
    sex: str
    blackcnt: int
    dormancyyn: int
    leaveyn: str
    banyn: str
    joindt: datetime
    createdt: datetime
    leavedt: datetime = None
    bandt: datetime = None
    image: str = None
    updatereason: str = None
    dormancyreason: str = None
    leavereason: str = None
    banreason: str = None

    # TODO: Config - 예시 파라미터
    class Config:
        json_schema_extra = {"example": {"id": 0, "item": "Example Schema!"}}
