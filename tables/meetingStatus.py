from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base


class MeetingStatus(Base):
    __tablename__ = "meetingStatus"

    id = Column(
        String,
        primary_key=True,
        unique=True,
    )
    status = Column(Integer)

    meetingStatus_meeting = relationship("Meeting", back_populates="meetingStatus")
