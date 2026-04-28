from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="test_worker_ping",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["debug"],
):
    BashOperator(
        task_id="ping_worker",
        bash_command='echo "hola desde $(hostname)" && sleep 5',
        queue="default",
    )
