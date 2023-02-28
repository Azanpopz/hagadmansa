import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class cred:
    BOT_NAME = os.getenv("BOT_NAME")
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # From botfather
    API_ID = os.getenv(
        "API_ID"
    )  # "Get this value from my.telegram.org! Please do not steal"
    API_HASH = os.getenv(
        "API_HASH"
    )  # "Get this value from my.telegram.org! Please do not steal"
    DATABASE_URL = os.getenv("DATABASE_URL")  # From Firebase database
