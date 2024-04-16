from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from mappers import get_all_members_mapper, get_member_mapper


async def get_all_members(db: Session):
    data = await db.execute(text(get_all_members_mapper()))

    return data.all()


async def get_member(db: Session):
    data = await db.execute(text(get_member_mapper(0)))

    return data.one()
