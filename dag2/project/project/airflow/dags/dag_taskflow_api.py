from datetime import datetime,timedelta
from airflow import DAG
from airflow.decorators import dag,task

default_args={
    "owner":"rohan patankar",
    "retries":5,
    "retry_delay":timedelta(minutes=1),
}

@dag(dag_id="dag_with_taskflow_api",default_args=default_args,start_date=datetime(2022,9,19,11,9),schedule_interval="@once")
def hello_world_etl():
    @task()
    def extract():
        return "extracted"
    @task()
    def transform():
        return "transformed"
    @task()
    def load():
        return "loaded"
    ext=extract()
    tra=transform()
    loa=load()
greet_dag=hello_world_etl()