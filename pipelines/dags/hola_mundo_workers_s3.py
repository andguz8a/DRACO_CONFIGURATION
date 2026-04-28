from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="hola_mundo_workers_s3",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["test", "workers", "s3"],
) as dag:
    tasks = []
    for i in range(1, 7):
        t = BashOperator(
            task_id=f"hola_{i}",
            bash_command=f'echo "Hola mundo desde Airflow task {i}"; echo "HOST=$(hostname)"; sleep 10',
            queue="default",
        )
        tasks.append(t)
