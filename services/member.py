from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from mappers.member import get_all_members_mapper, get_member_mapper


def get_all_members(db: Session):
    data = db.execute(text(get_all_members_mapper())).all()

    return data


def get_member(db: Session):
    data = db.execute(text(get_member_mapper(0))).one()

    return data
