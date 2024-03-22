from sqlalchemy.orm import Session
from tables.member import Member

def get_all_members(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Member).offset(skip).limit(limit).all()
