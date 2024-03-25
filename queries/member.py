from sqlalchemy.orm import Session
from tables.member import Member
from tables.degree import Degree
from tables.level import Level


def get_all_members(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Member).offset(skip).limit(limit).all()


def get_member(db: Session):
    return (
        db.query(Member)
        .join(Degree, Member.degreeFK == Degree.id)
        .join(Level, Member.levelFK == Level.id)
        .filter(Member.id == "0")
    )
