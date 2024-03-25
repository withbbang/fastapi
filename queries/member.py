from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from tables.member import Member
from database.connection import con

from tables.level import Level
from tables.degree import Degree


def get_all_members(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Member).offset(skip).limit(limit).all()


def get_member(db: Session):
    data = db.execute(
        text(
            """
        select
            *
        from
            member m
            join level l on m.levelFK = l.id
            join degree d on m.degreeFK = d.id
        """
        )
    ).one()

    return data


# def get_member():
#     sqlText = text(
#         """
#         select
#             *
#         from
#             member m
#             join level l on m.levelFK = l.id
#             join degree d on m.degreeFK = d.id
#         """
#     )
#     member = con.execute(sqlText)

#     print("data: ", member)

#     return member
