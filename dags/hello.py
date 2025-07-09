from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args ={
    'owner':'daemon',
    'start_date': datetime(2025,1,25),
    'catchup': False
}


dag = DAG(
    'Hello_World',
    default_args= default_args,
    schedule= timedelta(days=1)
)
task1 = BashOperator(
    task_id='hellow_owrld',
    bash_command='echo "Hello Daemon"',
    dag = dag
)

task2 = BashOperator(
    task_id='hellow_world',
    bash_command='echo "Hello World"',
    dag = dag
)

task1 >> task2