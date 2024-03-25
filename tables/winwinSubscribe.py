from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base
from tables.member import Member


# 상생 신청 테이블
class WinwinSubscribe(Base):
    __tablename__ = "winwinSubscribe"

    id = Column(
        String,
        primary_key=True,
        unique=True,
    )
    memberFK = Column(String, ForeignKey("member.id"), nullable=False)
    comment = Column(String)
    status = Column(String, default="W")

    member = relationship(Member, back_populates="member_winwinSubscribe")
