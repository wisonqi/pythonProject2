# You can use this section to suppress warnings generated by your code:
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

# FindSpark simplifies the process of using Apache Spark with Python

import findspark
findspark.init()

from pyspark.sql import SparkSession

#import functions/Classes for sparkml

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

# import functions/Classes for metrics
from pyspark.ml.evaluation import RegressionEvaluator

#Create SparkSession
#Ignore any warnings by SparkSession command

spark = SparkSession.builder.appName("Regressing using SparkML").getOrCreate()
##!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0231EN-SkillsNetwork/datasets/mpg.csv
mpg_data = spark.read.csv("mpg.csv", header=True, inferSchema=True)
mpg_data.printSchema()
mpg_data.show(5)
assembler = VectorAssembler(inputCols=["Cylinders", "Engine Disp", "Horsepower", "Weight", "Accelerate", "Year"], outputCol="features")
mpg_transformed_data = assembler.transform(mpg_data)
mpg_transformed_data.select("features","MPG").show()
(training_data, testing_data) = mpg_transformed_data.randomSplit([0.7, 0.3], seed=42)

lr = LinearRegression(featuresCol="features", labelCol="MPG")
model = lr.fit(training_data)
predictions = model.transform(testing_data)

evaluator = RegressionEvaluator(labelCol="MPG", predictionCol="prediction", metricName="r2")
r2 = evaluator.evaluate(predictions)
print("R Squared =", r2)

evaluator = RegressionEvaluator(labelCol="MPG", predictionCol="prediction", metricName="rmse")
rmse = evaluator.evaluate(predictions)
print("RMSE =", rmse)

evaluator = RegressionEvaluator(labelCol="MPG", predictionCol="prediction", metricName="mae")
mae = evaluator.evaluate(predictions)
print("MAE =", mae)

spark.stop()
