import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    PRODUCT_DB = os.getenv("PRODUCT_DB")
    ORDER_DB = os.getenv("ORDER_DB")


settings = Settings()