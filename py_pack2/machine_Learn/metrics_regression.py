# !pip install pandas==1.3.4
# !pip install scikit-learn==0.20.1
# !pip install numpy==1.21.6
import pandas as pd
from sklearn.linear_model import LinearRegression

# import functions for train test split

from sklearn.model_selection import train_test_split

# import functions for metrics
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from math import sqrt

import matplotlib.pyplot as plt


def warn(*args, **kwargs):
    pass


import warnings

warnings.warn = warn
warnings.filterwarnings('ignore')

URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0231EN-SkillsNetwork/datasets/mpg.csv"
# using the read_csv function in the pandas library, we load the data into a dataframe.
df = pd.read_csv(URL)
df.sample(5)
df.shape
df.plot.scatter(x="Weight", y="MPG")
##plt.show()

### Task 2 - Identify the target column and the data columns
y = df["MPG"]  # y is the target
X = df[["Horsepower", "Weight"]]  # X is the set of features

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
lr = LinearRegression()
lr.fit(X_train, y_train)
print(lr.score(X_test, y_test))
original_values = y_test
predicted_values = lr.predict(X_test)
##### R Squared
print(r2_score(original_values, predicted_values))
##### Mean Squared Error
print("mean方阵err：", mean_squared_error(original_values, predicted_values))  # Lower the value the better the model
##### Root Mean Squared Error
print("Root mean 方阵：", sqrt(mean_squared_error(original_values, predicted_values)))  # Lower the value the better the model
###Mean Absolute Error
print(" mean 完全方阵：",  mean_absolute_error(original_values, predicted_values))  # Lower the value the better the model
