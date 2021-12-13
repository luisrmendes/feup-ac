import re
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


Data = pd.read_csv(
        'csv_files/dataTrain.csv',
        sep= ',', header = None)

Data = Data.values[:, 1:]
Data = pd.DataFrame(Data)

scaler = MinMaxScaler()

for i in range(44):
    scaler.fit(Data[[i]])
    Data[[i]] = scaler.transform(Data[[i]])

k_rng = range(1, 20)
sse = []
for k in k_rng:
    km = KMeans(n_clusters = k).fit(Data)
    sse.append(km.inertia_)

plt.plot(k_rng, sse)
  
results = KMeans(n_clusters=8).fit_predict(Data)
kmeans = KMeans(n_clusters=8).fit(Data)
centroids = kmeans.cluster_centers_
print(results)

plt.scatter(Data[0], Data[2], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 2], c='red', s=50)
plt.show()
