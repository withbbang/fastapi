from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import SessionLocal, engine
from models.test import Test

test_router = APIRouter(tags=["Tests"])


def get_tests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Test).offset(skip).limit(limit).all()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@test_router.get("/", response_model=list[Test])
def read_tests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tests = get_tests(db, skip=skip, limit=limit)
    return tests
