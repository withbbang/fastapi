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


class Meeting(Base):
    __tablename__ = "meeting"

    id = Column(String, primary_key=True, unique=True, index=True)
    name = Column(String)
    memberFK = Column(String)
    climbingAreaFK = Column(String)
    createDt = Column(TIMESTAMP)
    hostDt = Column(TIMESTAMP)
    updateDt = Column(TIMESTAMP)
    deleteDt = Column(TIMESTAMP)
    criticalMeetingYn = Column(String)
    meetingStatusFK = Column(String)

    meeting_attend = relationship("Attend", back_populates="meeting")

    member = relationship("Member", back_populates="member_meeting")
    climbingArea = relationship("ClimbingArea", back_populates="climbingArea_meeting")
    meetingStatus = relationship(
        "MeetingStatus", back_populates="meetingStatus_meeting"
    )
