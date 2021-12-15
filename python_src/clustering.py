import matplotlib.pyplot as plt
from sklearn import cluster
from sklearn.cluster import KMeans, SpectralClustering, Birch, AgglomerativeClustering
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

#KMeans----------------------------------------------------

Data = pd.read_csv(
        'csv_files/dataTrain.csv',
        sep= ',', header = None)

Data = Data.values[:, 1:]
Data = pd.DataFrame(Data)
labels =['loan_ids',
'loan_dates',
'loan_ammounts',
'loan_durations',
'loan_payments',
'loan_status',
'account_dates',
'account_frequency',        
'transactions_number_per_account',
'last_transaction_date_per_account',
'transactions_last_balance_per_account',
'no_transactions_type_credit_per_account',
'no_transactions_type_withdrawal_per_account',
'avg_amount_of_transaction_credit_per_account',
'median_amount_of_transaction_credit_per_account',
'max_amount_of_transaction_credit_per_account',
'min_amount_of_transaction_credit_per_account',
'variance_amount_of_transaction_credit_per_account',
'avg_amount_of_transaction_withdrawal_per_account',
'median_amount_of_transaction_withdrawal_per_account',
'max_amount_of_transaction_withdrawal_per_account',
'min_amount_of_transaction_withdrawal_per_account',
'variance_amount_of_transaction_withdrawal_per_account',
'no_k_na_of_transaction_per_account',
'no_k_household_of_transaction_per_account',
'no_k_interest_credited_of_transaction_per_account',
'no_k_old_age_pension_of_transaction_per_account',
'no_k_insurrance_payment_of_transaction_per_account',
'no_k_payment_for_statement_of_transaction_per_account',
'no_k_sanction_interest_if_negative_balance_of_transaction_per_account',
'owner_district_n_inhab_per_account',
'owner_district_n_inhab_per_account',
'owner_district_n_inhab_per_account',
'owner_district_n_inhab_per_account',
'owner_district_n_mun_inhab_0_499_per_account',
'owner_district_n_mun_inhab_500_1999_per_account',
'owner_district_n_mun_inhab_2000_9999_per_account',
'owner_district_n_mun_inhab_10000_inf_per_account',
'owner_district_n_cities_per_account',
'owner_district_ratio_urban_inhab_per_account',
'owner_district_average_salary_per_account',
'owner_district_unemploymant_95_per_account',
'owner_district_unemploymant_96_per_account',
'owner_district_n_enterp_per_1000_per_account',
'owner_district_n_crimes_95_per_account',
'owner_district_n_crimes_96_per_account']

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

#n_clusters=2----------------------------------------------------------------------------
#KMeans----------------------------------------------------
kmeans_results = KMeans(n_clusters=2).fit_predict(Data)
kmeans = KMeans(n_clusters=2).fit(Data)
centroids = kmeans.cluster_centers_
print(kmeans_results)

#Birch-----------------------------------------------------
birch_results = Birch(n_clusters=2).fit_predict(Data)
birch = Birch(n_clusters=2).fit(Data)
print(birch_results)

#AgglomerativeClustering-----------------------------------
agg_results = AgglomerativeClustering(n_clusters=2).fit_predict(Data)
agglomerativeClustering = AgglomerativeClustering(n_clusters=2).fit(Data)
print(agg_results)

cluster_success_rate = [] 
for i in range(2):
    success = 0
    total = 0
    for j in range(len(kmeans_results)):
        if kmeans_results[j] == i:
            if Data[4][j] == 1:
                success = success+1
            total = total+1
    print(success,total)
    cluster_success_rate.append(success/total)
print(cluster_success_rate)

#n_clusters=3----------------------------------------------------------------------------
#KMeans----------------------------------------------------
kmeans_results_3c = KMeans(n_clusters=3).fit_predict(Data)
kmeans_3c = KMeans(n_clusters=3).fit(Data)
centroids = kmeans.cluster_centers_
print(kmeans_results_3c)

#Birch-----------------------------------------------------
birch_results_3c = Birch(n_clusters=3).fit_predict(Data)
birch_3c = Birch(n_clusters=3).fit(Data)
print(birch_results_3c)

#AgglomerativeClustering-----------------------------------
agg_results_3c = AgglomerativeClustering(n_clusters=3).fit_predict(Data)
agglomerativeClustering_3c = AgglomerativeClustering(n_clusters=3).fit(Data)
print(agg_results_3c)

cluster_success_rate = [] 
for i in range(3):
    success = 0
    total = 0
    for j in range(len(birch_results_3c)):
        if birch_results_3c[j] == i:
            if Data[4][j] == 1:
                success = success+1
            total = total+1
    print(success,total)
    cluster_success_rate.append(success/total)
print(cluster_success_rate)

#View graphs-----------------------------------------------------------------------
'''
for i in range(44):
    plt.scatter(Data[i], np.zeros_like(Data[i]) + 0, c= birch_results_3c.astype(float), s=50, alpha=0.5)
    fig = plt.gcf()
    fig.canvas.manager.set_window_title(labels[i+1])
    plt.show()
'''

#plt.scatter(Data[0], Data[2], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
#plt.scatter(centroids[:, 0], centroids[:, 2], c='red', s=50)
#plt.show()

#SpectralClustering----------------------------------------------------
'''
results1 = SpectralClustering(n_clusters=2).fit_predict(Data)
spectralClustering = SpectralClustering(n_clusters=2).fit(Data)
print(results1)
'''

#Buid csv----------------------------------------------------
'''
data = pd.read_csv(
        'csv_files/dataTrain.csv',
        sep= ',', header = None)

data[45] = kmeans_results
data[46] = agg_results
data[47] = birch_results
data[48] = kmeans_results_3c
data[49] = agg_results_3c
data[50] = birch_results_3c

data.to_csv('clustering.csv', index = False)
'''
