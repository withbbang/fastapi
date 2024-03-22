from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from database.connection import Base


class Degree(Base):
    __tablename__ = "degree"

    id = Column(
        String,
        primary_key=True,
        unique=True,
    )
    degree = Column(String)
    color = Column(String)

    degree_member = relationship("Member", back_populates="degree")
