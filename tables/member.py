from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.connection import Base


class Member(Base):
    __tablename__ = "member"

    id = Column(
        String,
        primary_key=True,
        unique=True,
    )
    name = Column(String)
    birthDt = Column(String)
    levelFK = Column(String)
    degreeFK = Column(String)
    phoneNo = Column(String)
    winwinYn = Column(String, default="N")
    sex = Column(String, default="M")
    blackCnt = Column(Integer, default=0)
    dormancyYn = Column(String, default="N")
    leaveYn = Column(String, default="N")
    banYn = Column(String, default="N")
    joinDt = Column(String)
    createDt = Column(String)
    updateDt = Column(String)
    leaveDt = Column(String)
    banDt = Column(String)
    image = Column(String)
    updateReason = Column(String)
    dormancyReason = Column(String)
    leaveReason = Column(String)
    banReason = Column(String)
