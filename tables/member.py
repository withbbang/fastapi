from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Date,
    TIMESTAMP,
)
from sqlalchemy.orm import relationship
from database.connection import Base
from tables.winwinSubscribe import WinwinSubscribe
from tables.admin import Admin
from tables.degree import Degree
from tables.level import Level


# 회원 테이블
class Member(Base):
    __tablename__ = "member"

    id = Column(String, primary_key=True, unique=True, index=True)
    name = Column(String)
    birthDt = Column(String)
    levelFK = Column(String, ForeignKey("level.id"), nullable=False)
    degreeFK = Column(String, ForeignKey("degree.id"), nullable=False)
    phoneNo = Column(String)
    winwinYn = Column(String, default="N")
    sex = Column(String, default="M")
    blackCnt = Column(Integer, default=0)
    dormancyYn = Column(String, default="N")
    leaveYn = Column(String, default="N")
    banYn = Column(String, default="N")
    joinDt = Column(Date)
    createDt = Column(TIMESTAMP)
    updateDt = Column(TIMESTAMP)
    leaveDt = Column(Date)
    banDt = Column(TIMESTAMP)
    image = Column(String)
    updateReason = Column(String)
    dormancyReason = Column(String)
    leaveReason = Column(String)
    banReason = Column(String)

    member_winwinSubscribe = relationship(
        WinwinSubscribe, back_populates="member", uselist=False
    )
    member_admin = relationship(Admin, back_populates="member")

    level = relationship(Level, back_populates="level_member")
    degree = relationship(Degree, back_populates="degree_member")
