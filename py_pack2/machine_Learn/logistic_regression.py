#pip install scikit-learn==0.20.1
import matplotlib.pyplot as plt

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

import pandas as pd
from sklearn.linear_model import LogisticRegression
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0231EN-SkillsNetwork/datasets/iris.csv"

# using the read_csv function in the pandas library, we load the data into a dataframe.
df = pd.read_csv(URL)
print(df.sample(5))
print(df.shape)
df.Species.value_counts().plot.bar()
plt.show()
# Task2 Identify the target column
target = df["Species"]
features = df[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]]
classifier = LogisticRegression()
classifier.fit(features,target)
classifier.score(features,target)#分数越高越好
print(classifier.predict([[5.4, 2.6, 4.1, 1.3]]))
