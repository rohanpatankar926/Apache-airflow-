from random import randint
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator,BranchPythonOperator
from airflow.operators.bash import BashOperator

def _train_model():
    return randint(1, 100)

def choose_best_model(ti):
    accuracies = ti.xcom_pull(task_ids=[
        'train_model_A',
        'train_model_B',
        'train_model_C',
    ])
    best_accuracy = max(accuracies)
    if (best_accuracy < 100):
        return 'accurate'
    return 'inaccurate'

with DAG("my_dag1",start_date=datetime(2022,9,19,11,9),schedule_interval="@once") as dag:
    tran_model_A=PythonOperator(
    task_id="train_model_A",
    python_callable=_train_model,
    )
    tran_model_B=PythonOperator(
    task_id="train_model_B",
    python_callable=_train_model,)

    tran_model_C=PythonOperator(
    task_id="train_model_C",
    python_callable=_train_model,)

    choose_best_model_=BranchPythonOperator(
    task_id="choose_best_model",    
    python_callable=choose_best_model
    )
    accurate=BashOperator(
    task_id="accurate",
    bash_command="echo 'accurate'",
    )
    inaccurate=BashOperator(
    task_id="inaccurate",
    bash_command="echo 'inaccurate'",
    )

    [tran_model_A,tran_model_B,tran_model_C]>>choose_best_model_>> [accurate,inaccurate]
