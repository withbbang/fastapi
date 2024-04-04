from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from tables.member import Member


def get_all_members(db: Session):
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
    ).all()

    return data


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
