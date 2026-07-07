import clickhouse_connect

from etl.config import Config
from etl.logger import get_logger
from etl.exceptions import ClickHouseConnectionError

logger = get_logger()


class ClickHouseClient:

    def __init__(self):

        self.client = None

    def connect(self):

        try:

            self.client = clickhouse_connect.get_client(

                host=Config.CLICKHOUSE_HOST,

                port=Config.CLICKHOUSE_PORT,

                username=Config.CLICKHOUSE_USER,

                password=Config.CLICKHOUSE_PASSWORD,

                database=Config.CLICKHOUSE_DATABASE

            )

            logger.info("Connected to ClickHouse.")

            return self.client

        except Exception as e:

            raise ClickHouseConnectionError(str(e))

    def health_check(self):

        result = self.client.query("SELECT 1")

        return result.result_rows[0][0] == 1


client = ClickHouseClient()