"""Airflow DAG skeleton for the e-commerce ETL pipeline."""

import os
from datetime import timedelta
from pathlib import Path

import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

from src.extract import extract_all
from src.load import load_all, run_quality_checks
from src.transform import transform_all
from src.validate import validate_all

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data"
STAGING_DIR = PROJECT_ROOT / "data" / "staging"
VALIDATED_DIR = PROJECT_ROOT / "data" / "validated"
TRANSFORMED_DIR = PROJECT_ROOT / "data" / "transformed"


def _load_data() -> int:
    """Load transformed records using the configured database connection."""
    database_url = os.environ["ECOMMERCE_DATABASE_URL"]
    return load_all(TRANSFORMED_DIR, database_url)


def _run_quality_checks() -> None:
    """Run post-load checks using the configured database connection."""
    database_url = os.environ["ECOMMERCE_DATABASE_URL"]
    run_quality_checks(database_url)


with DAG(
    dag_id="ecommerce_etl_pipeline",
    description="Extract, validate, transform, load, and check e-commerce data.",
    default_args={
        "owner": "data-engineering",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    tags=["ecommerce", "etl"],
) as dag:
    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_all,
        op_kwargs={"raw_dir": RAW_DATA_DIR, "staging_dir": STAGING_DIR},
    )

    validate = PythonOperator(
        task_id="validate",
        python_callable=validate_all,
        op_kwargs={"staging_dir": STAGING_DIR, "validated_dir": VALIDATED_DIR},
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=transform_all,
        op_kwargs={
            "validated_dir": VALIDATED_DIR,
            "transformed_dir": TRANSFORMED_DIR,
        },
    )

    load = PythonOperator(
        task_id="load",
        python_callable=_load_data,
    )

    quality_check = PythonOperator(
        task_id="quality_check",
        python_callable=_run_quality_checks,
    )

    extract >> validate >> transform >> load >> quality_check
