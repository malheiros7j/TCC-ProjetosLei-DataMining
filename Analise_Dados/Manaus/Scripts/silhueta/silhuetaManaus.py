#coding:utf-8

import matplotlib.pyplot as plt
import matplotlib.cm as cm

from matplotlib import style
style.use('ggplot')


import numpy as np
import pandas as pd
from numpy.random import RandomState
import sys

from sklearn import metrics
from sklearn.cluster import KMeans

from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.preprocessing import Normalizer


data = pd.read_csv('manaus.csv')
data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)
data.drop(data.columns[0], axis = 1, inplace = True)
##print(data)
##print(df.head())

n_samples, n_features = data.shape

#Realizar Normalizacao do Data
normalizer = Normalizer(copy=False)
date  = normalizer.fit_transform(data)

print("n_samples:%d \t n_features:%d" % (n_samples, n_features))
print(82 * '_')
print('\n')

###############################################################################################################################

range_n_clusters = [6,8,10,15,20,25,30]

for i in range(5):
    for n_clusters in range_n_clusters:

        clusterer = KMeans(n_clusters=n_clusters,init="k-means++")
        cluster_labels = clusterer.fit_predict(date)

        # Contabiliza e imprime o score da analise de silhueta
        silhouette_avg = silhouette_score(date, cluster_labels)
        print"For n_clusters =", n_clusters, "The average silhouette_score is :", silhouette_avg
    print('\n')




    #Cria o subgrafico para ilustrar a silhueta
    '''
    fig, (ax1) = plt.subplots(1)
    fig.set_size_inches(18, 7)

    # Define o limite dos valores da silhueta, no caso ela eh analisade de (-1,1) porem vamos utilizar de (-0,1,1)
    ax1.set_xlim([-0.1, 1])

    ax1.set_ylim([0, len(date) + (n_clusters + 1) * 10])

    clusterer = KMeans(n_clusters=n_clusters,init="k-means++")
    cluster_labels = clusterer.fit_predict(date)

    # Contabiliza e imprime o score da analise de silhueta
    silhouette_avg = silhouette_score(date, cluster_labels)
    print"For n_clusters =", n_clusters, "The average silhouette_score is :", silhouette_avg

    # Computa o valor da silhueta para cada amostra
    sample_silhouette_values = silhouette_samples(date, cluster_labels)

    y_lower = 10
    for i in range(n_clusters):
        # Agrega o score da silhueta para as entrrada pertencente ao cluster i, e ordena eles
        ith_cluster_silhouette_values = \
            sample_silhouette_values[cluster_labels == i]

        ith_cluster_silhouette_values.sort()

        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = cm.spectral( float(i) / n_clusters) 
        ax1.fill_betweenx(np.arange(y_lower, y_upper),
                          0, ith_cluster_silhouette_values,
                          facecolor=color, edgecolor=color, alpha=0.7)

        # Coloca o numero de cada cluster correspondente
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        
        y_lower = y_upper + 10 

    ax1.set_title("Grafico da silhueta dos diferentes clusters")
    ax1.set_xlabel("Valor dos coeficientes de silhueta")
    ax1.set_ylabel("Cluster label")

    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")
    ax1.set_yticks([])
    ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    plt.suptitle(("Analise da Silhueta para K-Means clustering"
                  "com n_clusters = %d" % n_clusters),
                 fontsize=14, fontweight='bold')

    plt.show()

'''