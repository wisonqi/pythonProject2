from pyspark.sql import SparkSession
from pyspark.sql.functions import col
# Create a Spark session
## 这个一直报错Accep timed out 不知道怎么解决
spark = SparkSession.builder.appName("CostBasedOptimization").getOrCreate()
# Sample input data for DataFrame 1
data1 = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 22),
    ("Diana", 28)
]
# Sample input data for DataFrame 2
data2 = [
    ("Alice", "New York"),
    ("Bob", "San Francisco"),
    ("Charlie", "Los Angeles"),
    ("Eve", "Chicago")
]
# Create DataFrames
columns1 = ["name", "age"]
df1 = spark.createDataFrame(data1, columns1)
columns2 = ["name", "city"]
df2 = spark.createDataFrame(data2, columns2)
# Enable adaptive query execution
spark.conf.set("spark.sql.adaptive.enabled", "true")
# Applying Adaptive Query Execution (Runtime adaptive optimization)
optimized_join = df1.join(df2, on="name")
# Show the optimized join result
print("Optimized Join DataFrame:")
optimized_join.show()
# Stop the Spark session
spark.stop()
