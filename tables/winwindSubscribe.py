from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base


# 상생 신청 테이블
class WinwindSubscribe(Base):
    __tablename__ = "winwindSubscribe"

    id = Column(
        String,
        primary_key=True,
        unique=True,
    )
    memberFK = Column(String, ForeignKey("member.id"), nullable=False)
    comment = Column(String)

    member = relationship("Member", back_populates="member_winwindSubscribe")
