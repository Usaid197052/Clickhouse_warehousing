import pandas as pd

from utils import get_logger

logger = get_logger(__name__)


def transform_data(df: pd.DataFrame):

    logger.info("Starting Transformation...")

    df = df.copy()

    df["brand"] = df["brand"].fillna("Unknown")

    df["category_code"] = df["category_code"].fillna("Unknown")

    logger.info("Transformation Complete")

    return df