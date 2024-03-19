import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

USERNAME = os.getenv("username")
PASSWORD = os.getenv("password")
DSN = os.getenv("dsn")
CONFIG_DIR = os.getenv("config_dir")
WALLET_LOCATION = os.getenv("wallet_location")
WALLET_PASSWORD = os.getenv("wallet_password")

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://url"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
