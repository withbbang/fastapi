import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("username")
PASSWORD = os.getenv("password")
DSN = os.getenv("dsn")
CONFIG_DIR = os.getenv("config_dir")
WALLET_LOCATION = os.getenv("wallet_location")
WALLET_PASSWORD = os.getenv("wallet_password")

connection = oracledb.connect(
    user=USERNAME,
    password=PASSWORD,
    dsn=DSN,
    config_dir=CONFIG_DIR,
    wallet_location=WALLET_LOCATION,
    wallet_password=WALLET_PASSWORD,
)

cursor = connection.cursor()
