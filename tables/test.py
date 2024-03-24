from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.connection import Base


class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True)
    name = Column(String)
