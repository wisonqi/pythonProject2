# Code for ETL operations on Bank data

# Importing the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime

url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ["Name", "MC_USD_Billion"]
db_name = 'Banks.db'
table_name = 'Largest_banks'
csv_path = 'Largest_banks_data.csv'
exchange_rate_path= 'exchange_rate.csv'
#set the max columns out put to console
pd.set_option('display.max_columns', 7)
def log_progress(message):
    ''' This function logs the mentioned message at a given stage of the code execution to a log file. Function returns nothing'''
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("code_log", "a") as f:
        f.write(timestamp + ' : ' + message + '\n')

def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    html_page = requests.get(url).text
    bs4= BeautifulSoup(html_page,'html.parser')
    df=pd.DataFrame(columns=table_attribs)
    col = bs4.find_all('tbody')
    #print(col)
    rows=col[0].find_all('tr')
    #print("col的类型是:"+str(type(col))) #bs4.element.ResultSet
    #print(rows)
    for row in rows:
        col = row.find_all('td')
        if len(col)!=0:
            #print(col[0])
            #if col[0].find('i') is not None:
            if col[1].find('a') is not None:
                data_dict = {"Name": col[1].find_all('a')[1]['title'], #这里取第二个，第一个标签是国家，第二个是银行
                             "MC_USD_Billion": float(col[2].contents[0][:-1])} #末尾有回车，消除掉
                #print(data_dict)
                #print(col[1])
                #print(col[2])
                #print("col1是:"+str(col[1]))
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df,df1], ignore_index=True)
    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''
    #set dict of exchange rate
    dict=pd.DataFrame(columns=('Currency','Rate'))
    with open(csv_path,'r') as rate:
        while 1==1:
            line_list=rate.readline().split(',')
            if len(line_list)>1:
                #print("this is an output:"+str(line_list))
                #print(line_list[1])
                new = pd.DataFrame({'Currency':line_list[0],'Rate':line_list[1][:-1]},index=[1])
                dict=dict._append(new,ignore_index='true')
                #print(dict)
            else: break
    dict = dict.set_index('Currency').to_dict()['Rate']
    #以上代码可以用以下两行来实现
    #exchange_df=pd.read_csv(csv_path)
    #exchange_dict=exchange_df.set_index('Currency').to_dict()['Rate']


    #add colums of df
    print(dict['GBP'])
    df['MC_GBP_Billion'] = [np.round(x*float(dict['GBP']),2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x*float(dict['EUR']),2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*float(dict['INR']),2) for x in df['MC_USD_Billion']]
    return df
def load_to_csv(df, output_path):
    df.to_csv(csv_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)
def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)
''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url,table_attribs)
#print(df)
log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df,exchange_rate_path)
#print(df)
log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df,csv_path)
#print(df['MC_EUR_Billion'][4])
log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect('Banks.db')
log_progress('SQL Connection initiated.')
load_to_db(df, sql_connection, table_name)
log_progress('Data loaded to Database as table. Running the query')

query_statement1 = f"SELECT * FROM {table_name}"
run_query(query_statement1, sql_connection)
query_statement2 = f"SELECT AVG(MC_GBP_Billion) FROM {table_name}"
run_query(query_statement2, sql_connection)
query_statement3 = f"SELECT Name from {table_name} LIMIT 5"
run_query(query_statement3, sql_connection)

log_progress('Process Complete.')

sql_connection.close()
