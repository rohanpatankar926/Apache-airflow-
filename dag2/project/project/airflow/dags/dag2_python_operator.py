from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def  divide(a, b):
    return a / b


with DAG("dag2",start_date=datetime(2022,9,19,11,9),schedule_interval="@once") as dag:
    add_=PythonOperator(task_id="add",python_callable=add,op_kwargs={"a":5,"b":10})
    subtract_=PythonOperator(task_id="subtract",python_callable=subtract,op_kwargs={"a":5,"b":10})
    multiply_=PythonOperator(task_id="multiply",python_callable=multiply,op_kwargs={"a":5,"b":10})
    divide_=PythonOperator(task_id="divide",python_callable=divide,op_kwargs={"a":5,"b":10})
    success=BashOperator(task_id="success",bash_command="echo success")
[add_,subtract_ , multiply_ , divide_]>>success