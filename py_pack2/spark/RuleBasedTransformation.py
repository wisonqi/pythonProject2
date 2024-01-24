from pyspark.sql import SparkSession
from pyspark.sql.functions import col
# Create a Spark session
spark = SparkSession.builder.appName("RuleBasedTransformations").getOrCreate()
# Sample input data for DataFrame 1
data1 = [
    ("Alice", 25, "F"),
    ("Bob", 30, "M"),
    ("Charlie", 22, "M"),
    ("Diana", 28, "F")
]
# Sample input data for DataFrame 2
data2 = [
    ("Alice", "New York"),
    ("Bob", "San Francisco"),
    ("Charlie", "Los Angeles"),
    ("Eve", "Chicago")
]
# Create DataFrames
columns1 = ["name", "age", "gender"]
df1 = spark.createDataFrame(data1, columns1)
columns2 = ["name", "city"]
df2 = spark.createDataFrame(data2, columns2)
# Applying Predicate Pushdown (Filtering)
filtered_df = df1.filter(col("age") > 25)
# Applying Constant Folding
folded_df = filtered_df.select(col("name"), col("age") + 2)
# Applying Column Pruning
pruned_df = folded_df.select(col("name"))
# Join Reordering
reordered_join = df1.join(df2, on="name")
# Show the final results
print("Filtered DataFrame:")
filtered_df.show()
print("Folded DataFrame:")
folded_df.show()
print("Pruned DataFrame:")
pruned_df.show()
print("Reordered Join DataFrame:")
reordered_join.show()
# Stop the Spark session
spark.stop()
