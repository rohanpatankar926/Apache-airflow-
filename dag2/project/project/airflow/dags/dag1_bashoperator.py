from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    "owner":"rohan patankar",
    "retries":5,
    "retry_delay":timedelta(minutes=1),
    
}

with DAG("my_dag",start_date=datetime(2022,9,19,11,9),schedule_interval="@once") as dag:
    task1=BashOperator(
        task_id="task1",
        bash_command="echo 'hello world'"
)
    task2=BashOperator(
        task_id="task2",
        bash_command="echo 'hello rohan'"
    )

    task1>>task2