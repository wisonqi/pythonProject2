import findspark

findspark.init()

import pandas as pd
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark DataFrames basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

spark

mtcars = pd.read_csv(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/mtcars.csv')
mtcars.head()
sdf = spark.createDataFrame(mtcars)
sdf.printSchema()
sdf.show(5)
sdf.select('mpg').show(5)
sdf.filter(sdf['mpg'] < 18).show(5)
sdf_new = sdf.withColumnRenamed("vs", "versus")
sdf.where(sdf['mpg'] < 18).show(3)
###### Task 5: Combining DataFrames based on a specific condition.

data = [("A101", "John"), ("A102", "Peter"), ("A103", "Charlie")]

columns = ["emp_id", "emp_name"]

dataframe_1 = spark.createDataFrame(data, columns)
data = [("A101", 1000), ("A102", 2000), ("A103", 3000)]

columns = ["emp_id", "salary"]

dataframe_2 = spark.createDataFrame(data=data, schema=columns) ##这里直接用data和column就好，这个等于是我加上去的
combined_df = dataframe_1.join(dataframe_2, on="emp_id", how="inner")
data = [("A101", 1000), ("A102", 2000), ("A103", None)]

columns = ["emp_id", "salary"]
# "fillna()" or "fill()" function fill the missing values with a specified value.

dataframe_1 = spark.createDataFrame(data, columns)
filled_df = dataframe_1.fillna({"salary": 3000})
filled_df.head(3)
##### Exercise 4: Grouping and Aggregation
sdf.groupby(['cyl']) \
    .agg({"wt": "AVG"}) \
    .show(5)

car_counts = sdf.groupby(['cyl']) \
    .agg({"wt": "count"}) \
    .sort("count(wt)", ascending=False) \
    .show(5)
