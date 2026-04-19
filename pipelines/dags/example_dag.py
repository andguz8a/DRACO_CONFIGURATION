from airflow.decorators import dag, task
from datetime import datetime
from pipelines.tasks.hello_task import get_server_info


@dag(
    dag_id="example_hello_world",
    schedule=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["example"],
)
def example_dag():

    @task
    def hello():
        return get_server_info()

    hello()


dag_instance = example_dag()