import sys
sys.path.append("/mnt/Work/Master/SS-23/SAKI/2023-amse-template/Data")

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from pathlib import Path

from api_data_getter import get_data


with DAG(dag_id="SAKI",
         start_date=datetime(2023, 5, 25),
         schedule="@hourly",
         catchup=False) as dag:
    task1 = PythonOperator(
        task_id="fetcher_inserter",
        python_callable=get_data)

task1
