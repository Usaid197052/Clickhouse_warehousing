from pathlib import Path

from etl.config import Config

from etl.logger import get_logger

from etl.sql_executor import SQLExecutor

from etl.validation import Validator

logger = get_logger()


class ELTPipeline:

    def __init__(self):

        self.sql = SQLExecutor()

        self.validator = Validator()

        self.sql_path = Path(Config.SQL_PATH)

    def run(self):

        logger.info("=" * 60)

        logger.info("Starting ELT Pipeline")

        logger.info("=" * 60)

        self.sql.execute_file(self.sql_path / "00_init.sql")

        self.sql.execute_file(self.sql_path / "01_staging.sql")

        self.sql.execute_file(self.sql_path / "02_dimensions.sql")

        self.sql.execute_file(self.sql_path / "03_fact_events.sql")

        self.sql.execute_file(self.sql_path / "04_materialized_views.sql")

        self.sql.execute_file(self.sql_path / "05_data_marts.sql")

        self.sql.execute_file(self.sql_path / "06_quality_checks.sql")

        logger.info("=" * 60)

        logger.info("Pipeline Complete")

        logger.info("=" * 60)


def run_pipeline():

    ELTPipeline().run()


if __name__ == "__main__":

    run_pipeline()