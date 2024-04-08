import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
con = engine.connect()
Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()


# Dependency
def get_db():
    db = Session()
    try:
        yield db
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        raise Exception
    finally:
        print("db: ", db)
        db.close()
