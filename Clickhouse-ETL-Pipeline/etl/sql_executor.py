from pathlib import Path
from time import perf_counter

import sqlparse

from etl.clickhouse_client import client
from etl.exceptions import SQLExecutionError
from etl.logger import get_logger

logger = get_logger()


class SQLExecutor:

    def __init__(self):
        self.client = client.connect()

    def execute(self, sql: str):

        try:

            start = perf_counter()

            self.client.command(sql)

            end = perf_counter()

            logger.info(
                f"Completed in {end - start:.2f} seconds"
            )

            return True

        except Exception as e:

            logger.error(e)

            raise SQLExecutionError(str(e))

    def execute_file(self, file_path):

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(path)

        logger.info(f"Executing {path.name}")

        sql = path.read_text(encoding="utf-8")

        statements = sqlparse.split(sql)

        for statement in statements:

            statement = statement.strip()

            if not statement:
                continue

            logger.info(
                f"Running statement: {statement.splitlines()[0][:80]}"
            )

            self.execute(statement)

        return True

    def execute_directory(self, directory):

        directory = Path(directory)

        sql_files = sorted(directory.glob("*.sql"))

        results = []

        logger.info("=" * 60)

        logger.info(f"Found {len(sql_files)} SQL files.")

        logger.info("=" * 60)

        for file in sql_files:

            logger.info("-" * 60)

            logger.info(f"Running {file.name}")

            status = self.execute_file(file)

            results.append(
                {
                    "file": file.name,
                    "status": status
                }
            )

        logger.info("=" * 60)

        logger.info("SQL execution complete.")

        logger.info("=" * 60)

        return results