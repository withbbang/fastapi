import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("username")
PASSWORD = os.getenv("password")
DSN = os.getenv("dsn")
CONFIG_DIR = os.getenv("config_dir")
WALLET_LOCATION = os.getenv("wallet_location")
WALLET_PASSWORD = os.getenv("wallet_password")
