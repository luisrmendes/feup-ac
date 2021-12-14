import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, SpectralClustering, Birch
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#KMeans----------------------------------------------------

Data = pd.read_csv(
        'csv_files/dataTrain.csv',
        sep= ',', header = None)

Data = Data.values[:, 1:]
Data = pd.DataFrame(Data)

scaler = MinMaxScaler()

for i in range(44):
    scaler.fit(Data[[i]])
    Data[[i]] = scaler.transform(Data[[i]])

k_rng = range(1, 10)
sse = []
for k in k_rng:
    km = KMeans(n_clusters = k)
    km.fit(Data)
    sse.append(km.inertia_)

plt.plot(k_rng, sse)
plt.show()

  
results = KMeans(n_clusters=2).fit_predict(Data)
kmeans = KMeans(n_clusters=2).fit(Data)
centroids = kmeans.cluster_centers_
print(results)

#plt.scatter(Data[0], Data[2], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
#plt.scatter(centroids[:, 0], centroids[:, 2], c='red', s=50)
#plt.show()


#SpectralClustering----------------------------------------------------
results1 = SpectralClustering(n_clusters=2).fit_predict(Data)
spectralClustering = SpectralClustering(n_clusters=2).fit(Data)
print(results1)


#Birch----------------------------------------------------
results2 = Birch(n_clusters=None).fit_predict(Data)
birch = Birch(n_clusters=None).fit(Data)
print(results2)

data = pd.read_csv(
        'csv_files/dataTrain.csv',
        sep= ',', header = None)

data[45] = results
data[46] = results1
data[47] = results2

print (data)

data.to_csv('clustering.csv', index = False)
