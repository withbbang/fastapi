from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from mappers.test import add_test_mapper
from decoraters.transactional import Transactional


@Transactional()
async def raise_add_test(db: Session):
    import asyncio

    print("raise_add_test service: ", db)
    db.execute(text(add_test_mapper(4)))

    await asyncio.sleep(3)

    raise Exception


@Transactional()
async def add_test(db: Session):
    import asyncio

    print("add_test service: ", db)
    db.execute(text(add_test_mapper(5)))
