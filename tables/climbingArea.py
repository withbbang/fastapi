from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base
from tables import Meeting


# 암장 테이블
class ClimbingArea(Base):
    __tablename__ = "climbingArea"

    id = Column(
        String,
        primary_key=True,
        unique=True,
    )
    climbingAreaName = Column(String)
    price = Column(String)
    address = Column(String)
    winwinYn = Column(String)
    createDt = Column(TIMESTAMP)
    updateDt = Column(TIMESTAMP)

    climbingArea_meeting = relationship(Meeting, back_populates="climbingArea")
