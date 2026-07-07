import clickhouse_connect

from config import CLICKHOUSE_CONFIG
from utils import get_logger

logger = get_logger(__name__)


def extract_data(query: str):

    logger.info("Connecting to ClickHouse...")

    client = clickhouse_connect.get_client(
        host=CLICKHOUSE_CONFIG["host"],
        port=CLICKHOUSE_CONFIG["port"],
        username=CLICKHOUSE_CONFIG["username"],
        password=CLICKHOUSE_CONFIG["password"],
        database=CLICKHOUSE_CONFIG["database"],
    )

    logger.info("Executing Query...")

    result = client.query_df(query)

    logger.info(f"Extracted {len(result)} rows")

    return result