import findspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

findspark.init()

# Creating a spark context class
sc = SparkContext()

# Creating a spark session
spark = SparkSession \
    .builder \
    .appName("Python Spark DataFrames basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# print(spark)
numbers = range(1, 50)
numbers_RDD = sc.parallelize(numbers, 2)
even_numbers_RDD = numbers_RDD.map(lambda x: x * 2)
print(even_numbers_RDD.collect())


##spark.stop() ##will stop the spark session

