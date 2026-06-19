from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'aditya',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'my_first_pipeline',
    default_args=default_args,
    description='First working pipeline',
    schedule_interval=None,  # Manual trigger only
    catchup=False,
) as dag:

    task_1 = BashOperator(
        task_id='print_hello',
        bash_command='echo "Hello World from Airflow!"',
    )

    task_2 = BashOperator(
        task_id='print_complete',
        bash_command='echo "Pipeline executed successfully."',
    )

    task_1 >> task_2  # Sets task_1 to run before task_2
