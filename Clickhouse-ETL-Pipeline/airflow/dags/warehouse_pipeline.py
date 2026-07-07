from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from etl.pipeline import run_pipeline

default_args = {
    "owner": "Usaid",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="warehouse_pipeline",
    description="ClickHouse ETL Pipeline",
    default_args=default_args,
    start_date=datetime(2026, 7, 1),
    schedule="@daily",
    catchup=False,
    tags=["clickhouse", "etl"],
) as dag:

    run_pipeline_task = PythonOperator(
        task_id="run_pipeline",
        python_callable=run_pipeline,
    )