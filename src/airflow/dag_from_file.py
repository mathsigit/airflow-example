from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from dag_default_args import default_args

dag = DAG(
    'write2hadoop',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(minutes=10),
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
    bash_command='export JAVA_HOME=/usr/local/zulu8 && bash /usr/local/airflow/hadoop-2.8.5/bin/hadoop jar /usr/local/airflow/hadoop-example-1.0-SNAPSHOT.jar com.stana.hadoop.Write2HDFS',
    dag=dag,
)

dag.doc_md = __doc__

t1.doc_md = """\
#### Task go_to_application_dir Documentation
This is a dummy task, doing nothing but going to the folder of `/usr/local/airflow`.
"""

t2.doc_md = """\
#### Task read_file_and_write_to_hadoop Documentation
Executing the hadoop jar command.
"""

t1 >> t2