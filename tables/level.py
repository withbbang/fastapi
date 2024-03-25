from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from database.connection import Base


# 회원 레벨 테이블
class Level(Base):
    __tablename__ = "level"

    id = Column(
        String,
        primary_key=True,
        unique=True,
    )
    level = Column(String)
    color = Column(String)

    level_member = relationship("Member", back_populates="level")
