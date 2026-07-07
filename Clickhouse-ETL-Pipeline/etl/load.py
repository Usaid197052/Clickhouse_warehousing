import clickhouse_connect

from config import CLICKHOUSE_CONFIG
from utils import get_logger

logger = get_logger(__name__)


def load_dataframe(df, table_name):

    client = clickhouse_connect.get_client(
        host=CLICKHOUSE_CONFIG["host"],
        port=CLICKHOUSE_CONFIG["port"],
        username=CLICKHOUSE_CONFIG["username"],
        password=CLICKHOUSE_CONFIG["password"],
        database=CLICKHOUSE_CONFIG["database"],
    )

    logger.info(f"Loading into {table_name}")

    client.insert_df(table_name, df)

    logger.info("Load Complete")