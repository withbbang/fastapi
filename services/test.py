from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from mappers import add_test_mapper
from decoraters import Transactional
import asyncio


@Transactional()
async def raise_add_test(db: Session):
    print("raise_add_test service: ", db)
    db.execute(text(add_test_mapper(4)))

    await asyncio.sleep(3)

    raise Exception("test error")


@Transactional()
async def add_test(db: Session):

    print("add_test service: ", db)
    db.execute(text(add_test_mapper(5)))
