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


class Member(Base):
    __tablename__ = "member"

    id = Column(String, primary_key=True, unique=True, index=True)
    name = Column(String)
    birthDt = Column(Date)
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

    member_winwindSubscribe = relationship("WinwindSubscribe", back_populates="member")
    member_admin = relationship("Admin", back_populates="member")

    level = relationship("Level", back_populates="level_member")
    degree = relationship("Degree", back_populates="degree_member")
