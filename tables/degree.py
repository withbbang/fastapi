from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from database.connection import Base
from tables.member import Member


# 기수 테이블
class Degree(Base):
    __tablename__ = "degree"

    id = Column(
        String,
        primary_key=True,
        unique=True,
    )
    degree = Column(String)
    description = Column(String)

    degree_member = relationship(Member, back_populates="degree")
