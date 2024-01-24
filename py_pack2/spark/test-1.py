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
data = range(1, 30)
# print first element of iterator
print(data[0])
len(data)
xrangeRDD = sc.parallelize(data, 4)

# this will let us know that we created an RDD
print(xrangeRDD)

subRDD = xrangeRDD.map(lambda x: x - 1)
filteredRDD = subRDD.filter(lambda x: x < 10)
print(filteredRDD.collect())
print(filteredRDD.count())

##--Excercise 3 对比缓存过一次之后的操作耗时，第二次操作明显耗时少了
import time

test = sc.parallelize(range(1,50000),4)
test.cache()

t1 = time.time()
# first count will trigger evaluation of count *and* cache
count1 = test.count()
dt1 = time.time() - t1
print("dt1: ", dt1)


t2 = time.time()
# second count operates on cached data only
count2 = test.count()
dt2 = time.time() - t2
print("dt2: ", dt2)

#test.count()
#### Task 1: Create Your First DataFrame!
df = spark.read.json("people.json").cache()
df.show()
df.printSchema()
df.createTempView("people")
##Task 2: Explore the data using DataFrame functions and SparkSQL¶
df.select("name").show()
df.select(df["name"]).show()
spark.sql("SELECT name FROM people").show()
df.filter(df["age"] > 21).show()
spark.sql("SELECT age, name FROM people WHERE age > 21").show()
df.groupBy("age").count().show()
spark.sql("SELECT age, COUNT(age) as count FROM people GROUP BY age").show()
