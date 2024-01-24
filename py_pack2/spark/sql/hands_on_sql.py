import findspark

findspark.init()
import pandas as pd
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

sc = SparkContext()

# Creating a spark session
spark = SparkSession \
    .builder \
    .appName("Python Spark DataFrames basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
# Read the file using `read_csv` function in pandas
mtcars = pd.read_csv(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/mtcars.csv')
# Preview a few records
print(mtcars.head())
mtcars.rename(columns={'Unnamed: 0': 'name'}, inplace=True)
sdf = spark.createDataFrame(mtcars)
sdf.printSchema()
sdf_new = sdf.withColumnRenamed("vs", "versus")
print(sdf_new.head(5))
sdf.createTempView("cars")
spark.sql("SELECT * FROM cars").show()
spark.sql("SELECT mpg FROM cars").show(5)
spark.sql("SELECT * FROM cars where mpg>20 AND cyl < 6").show(5)
sdf.where(sdf['mpg'] < 18).show(3)
spark.sql("SELECT count(*), cyl from cars GROUP BY cyl").show()
#####Create a Pandas UDF to apply a columnar operation
# import the Pandas UDF function
from pyspark.sql.functions import pandas_udf, PandasUDFType


@pandas_udf("float")
def convert_wt(s: pd.Series) -> pd.Series:
    # The formula for converting from imperial to metric tons
    return s * 0.45


# Applying the UDF to the tableview
spark.udf.register("convert_weight", convert_wt)
spark.sql("SELECT *, wt AS weight_imperial, convert_weight(wt) as weight_metric FROM cars").show()
#Combining DataFrames based on a specific condition.尝试join操作
# define sample DataFrame 1
data = [("A101", "John"), ("A102", "Peter"), ("A103", "Charlie")]
columns = ["emp_id", "emp_name"]
dataframe_1 = spark.createDataFrame(data, columns)

data = [("A101", 3250), ("A102", 6735), ("A103", 8650)]
columns = ["emp_id", "salary"]
dataframe_2 = spark.createDataFrame(data, columns)
combined_df = dataframe_1.join(dataframe_2, on="emp_id", how="inner")
print(combined_df.collect())
