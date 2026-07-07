from etl.clickhouse_client import client
from etl.logger import get_logger

logger = get_logger()


class Validator:

    def __init__(self):

        self.client = client.connect()

    def row_count(self, table):

        result = self.client.query(
            f"SELECT count() FROM {table}"
        )

        count = result.result_rows[0][0]

        logger.info(f"{table}: {count:,} rows")

        return count

    def query(self, sql):

        result = self.client.query(sql)

        return result.result_rows