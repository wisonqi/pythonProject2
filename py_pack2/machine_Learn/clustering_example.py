def warn(*args, **kwargs):
    pass


import warnings

warnings.warn = warn
warnings.filterwarnings('ignore')

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# the data set is available at the url below.
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0231EN-SkillsNetwork/datasets/customers.csv"

# using the read_csv function in the pandas library, we load the data into a dataframe.
df = pd.read_csv(URL)
print(df.sample(5))
df.shape
print(df.hist())
number_of_clusters = 3
cluster = KMeans(n_clusters=number_of_clusters)
result = cluster.fit_transform(df)
print(cluster.cluster_centers_)
#Make the predictions and save them into the column "cluster_number"
df['cluster_number'] = cluster.predict(df)
print(df.sample(5))
#Print the cluster numbers and the number of customers in each cluster
print(df.cluster_number.value_counts())
