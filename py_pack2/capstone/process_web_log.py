from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# set default args
##这个需要在airflow里面当作dag运行
default_args = {
    'owner': 'Ynayushu',  # set owner
    'start_date': datetime(2024, 1, 1),  # begin data
    'email': ['your_email@example.com'],  # mail
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),  # retry duration
}

# create DAG
dag = DAG(
    'my_dag',  # DAG unique id
    default_args=default_args,
    description='Capstone Project DAG',
    schedule_interval=timedelta(days=1),  # set schedule duration
)

# extract data
extract_data = BashOperator(
    task_id='extract_data',
    bash_command='grep -oE "^([0-9]{1,3}\.){3}[0-9]{1,3}" /home/project/airflow/dags/capstone/accesslog.txt > /home/project/airflow/dags/capstone/extracted_data.txt',
    ##使用cut -d " " -f1  这个命令也可以提取
    dag=dag
)
# transformdata
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='grep -v 198.46.149.143 /home/project/airflow/dags/capstone/extracted_data.txt > /home/project/airflow/dags/capstone/transformed_data.txt',
    dag=dag,
)
# load data
load_data = BashOperator(
    task_id="load_data",
    bash_command='cd /home/project/airflow/dags/capstone && tar -cvf weblog.tar transformed_data.txt',
    dag=dag,

)

# set pipeline
extract_data >> transform_data >> load_data
