from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from dag_default_args import default_args

dag = DAG(
    'write2hadoop',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(minutes=1),
)

t1 = BashOperator(
    task_id='go_to_application_dir',
    bash_command='cd /usr/local/airflow',
    dag=dag,
)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t2 = BashOperator(
    task_id='read_file_and_write_to_hadoop',
    depends_on_past=True,
    bash_command='hadoop jar hadoop-example-1.0-SNAPSHOT.jar com.stana.hadoop.Write2HDFS',
    dag=dag,
)

t1 >> t2