# Import libraries required for connecting to mysql

# Import libraries required for connecting to DB2 or PostgreSql

# Connect to MySQL

# Connect to DB2 or PostgreSql

# Find out the last rowid from DB2 data warehouse or PostgreSql data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database or PostgreSql.

import psycopg2
import mysql.connector

dsn_hostname = '127.0.0.1'
dsn_user = 'postgres'  # e.g. "abc12345"
dsn_pwd = 'MTc1NjktbWF3ZWl4'  # e.g. "7dBZ3wWt9XN6$o0J"
dsn_port = "5432"  # e.g. "50000"
dsn_database = "postgres"  # i.e. "BLUDB"

# create connection

conn = psycopg2.connect(
    database=dsn_database,
    user=dsn_user,
    password=dsn_pwd,
    host=dsn_hostname,
    port=dsn_port
)


# Crreate a cursor onject using cursor() method


def get_last_rowid():
    cursor = conn.cursor()
    ##sql = """select max(rowid) from sales_data;"""
    cursor.execute('select max(rowid) from sales_data;')
    conn.commit
    rows = cursor.fetchall()
    if rows:
        max_rowid = rows[0][0]
    return max_rowid


last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)


# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):
    connection = mysql.connector.connect(user='root', password='MzAyNDItbWF3ZWl4', host='127.0.0.1', database='sales')
    cursor = connection.cursor()
    sql = "select * from sales_data  where rowid > %s"
    cursor.execute(sql, (rowid,))
    rows = cursor.fetchall()
    return rows


new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", len(new_records))


# Insert the additional records from MySQL into DB2 or PostgreSql data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database or PostgreSql.

def insert_records(records):
    cursor = conn.cursor()
    sql = "INSERT INTO public.sales_data(rowid, product_id, customer_id, price,\
    quantity,\"timestamp\")VALUES (%s,%s,%s,0,%s,NOW());"
    for record in records:
        print(record)
        cursor.execute(sql, record)
    ##cursor.executemany(sql,records) #这里以为错了，还以为说的tuple越界是数据量太大，后来发现是参数对不上，修改上面的sql插入语句
    conn.commit()
    conn.close()


insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse

# disconnect from DB2 or PostgreSql data warehouse 

# End of program
