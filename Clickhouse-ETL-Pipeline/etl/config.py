import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    # ClickHouse
    CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST", "clickhouse")
    CLICKHOUSE_PORT = int(os.getenv("CLICKHOUSE_PORT", 8123))
    CLICKHOUSE_DATABASE = os.getenv("CLICKHOUSE_DATABASE", "ecommerce")
    CLICKHOUSE_USER = os.getenv("CLICKHOUSE_USER", "admin")
    CLICKHOUSE_PASSWORD = os.getenv("CLICKHOUSE_PASSWORD", "admin")

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # SQL Folder
    SQL_PATH = os.getenv("SQL_PATH", "./sql")