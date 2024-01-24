# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago
import pandas as pd
##这个是airflow的测验项目代码

#defining DAG arguments
default_args = {
    'owner': 'Ronald Churchill',
    'start_date': days_ago(0),
    'email': ['i_love_you@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# define the DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)

# define the tasks

# define the first task
unzip_data = BashOperator(
    task_id='unzip',
    bash_command='tar -zxvf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment/',
    dag=dag,
)

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cd /home/project/airflow/dags/finalassignment/ && cut -d "," -f1-4 vehicle-data.csv > csv_data.csv',
    dag=dag,
)

extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command='cut -f5-7 tollplaza-data.tsv |tr "\t" "," > tsv_data.csv',
    dag=dag,
)

extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command='cut -c 59-67 payment-data.txt |tr " " "," > fixed_width_data.csv',
    dag=dag,
)

consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command='paste -d ","  csv_data.csv tsv_data.csv fixed_width_data.csv > extracted_data.csv',
    dag=dag
)

##这里或者用cat命令加上tr a-z A-Z输出
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='awk -F \',\' \'{OFS=","; $4=toupper($4)}1\' "extracted_data.csv" > "transformed_data.csv"',
    dag=dag,
)

# task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data
