from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from tables import Member


# 관리자 계정 테이블
class Admin(Base):
    __tablename__ = "admin"

    id = Column(
        String,
        primary_key=True,
        unique=True,
    )
    memberFK = Column(String, ForeignKey("member.id"), nullable=False)
    memberId = Column(String, unique=True)
    password = Column(String)
    grade = Column(Integer, default=50)

    member = relationship(Member, back_populates="member_admin")
