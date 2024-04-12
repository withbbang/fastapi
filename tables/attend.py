from sqlalchemy import Column, String, ForeignKey
from database import Base


# 참석 테이블
class Attend(Base):
    __tablename__ = "attend"

    id = Column(
        String,
        primary_key=True,
        unique=True,
    )
    meetingFK = Column(String, ForeignKey("meeting.id"), nullable=False)
    memberFK = Column(String, ForeignKey("member.id"), nullable=False)
