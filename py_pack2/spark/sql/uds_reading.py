from pyspark.sql.types import StructType, IntegerType, FloatType, StringType, StructField
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

##这个文件是为了测试用户定义的结构 user defined structure

sc = SparkContext()
# Creating a spark session
spark = SparkSession \
    .builder \
    .appName("Python Spark DataFrames basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

schema = StructType([
    StructField("Emp_Id", StringType(), False),
    StructField("Emp_Name", StringType(), False),
    StructField("Department", StringType(), False),
    StructField("Salary", IntegerType(), False),
    StructField("Phone", IntegerType(), True),
])
# 'False' indicates null values are NOT allowed for the column.

# create a dataframe on top a csv file
df = (spark.read
      .format("csv")
      .schema(schema)
      .option("header", "true")
      .load("employee.csv")
      )
# display the dataframe content
df.show()

df.printSchema()
