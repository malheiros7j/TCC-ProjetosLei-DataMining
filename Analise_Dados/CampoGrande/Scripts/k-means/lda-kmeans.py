import numpy as np 
import pandas as pd

import matplotlib.pyplot as plt
import sys

from sklearn.preprocessing import Normalizer
from sklearn.decomposition import LatentDirichletAllocation


from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster

from sklearn.cluster import KMeans


data = pd.read_csv("cg.csv")
data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)
data.drop(data.columns[0], axis = 1, inplace = True)

n_samples, n_features = data.shape

# Normalizacao dos Dados
normalizer = Normalizer(copy=False)
date = normalizer.fit_transform(data)


print("n_documentos:%d \t n_palavras: %d \t " % (n_samples, n_features))
print(82 * '_')
print('\n')



clusterer = KMeans(n_clusters = 15, init="k-means++")
cluster_labels = clusterer.fit_predict(date)

cluster0 = []
cluster1 = []
cluster2 = []
cluster3 = []
cluster4 = []
cluster5 = []
cluster6 = []
cluster7 = []
cluster8 = []
cluster9 = []
cluster10 = []
cluster11 = []
cluster12 = []
cluster13 = []
cluster14 = []


for i in range(len(cluster_labels)):

	if cluster_labels[i] == 0:
		cluster0.append(date[i])

	elif cluster_labels[i] == 1:
		cluster1.append(date[i])

	elif cluster_labels[i] == 2:
		cluster2.append(date[i])

	elif cluster_labels[i] == 3:
		cluster3.append(date[i])

	elif cluster_labels[i] == 4:
		cluster4.append(date[i])

	elif cluster_labels[i] == 5:
		cluster5.append(date[i])

	elif cluster_labels[i] == 6:
		cluster6.append(date[i])

	elif cluster_labels[i] == 7:
		cluster7.append(date[i])

	elif cluster_labels[i] == 8:
		cluster8.append(date[i])

	elif cluster_labels[i] == 9:
		cluster9.append(date[i])

	elif cluster_labels[i] == 10:
		cluster10.append(date[i])

	elif cluster_labels[i] == 11:
		cluster11.append(date[i])

	elif cluster_labels[i] == 12:
		cluster12.append(date[i])

	elif cluster_labels[i] == 13:
		cluster13.append(date[i])

	elif cluster_labels[i] == 14:
		cluster14.append(date[i])

clusterizacao = [cluster0, cluster1, cluster2, cluster3, cluster4, cluster5, cluster6, cluster7, cluster8, cluster9, cluster10, cluster11, cluster12, cluster13, cluster14]

'''
orig_stdout = sys.stdout
f = open('clusters_labels.txt', 'w')
sys.stdout = f

for x in cluster_labels:
    print x

sys.stdout = orig_stdout
f.close()
'''

n_components = 5
n_top_words = 5

def print_top_words(model, feature_names, n_top_words):
	f  = open('stemWdST.all', 'r')
	content = f.readlines()
	dictionary = {}

	for line in content:
		palavras = line.split(' ')

		if(palavras[0] == ''):
			derivacao = palavras[-1].split(':')
			#print int(derivacao[1])
			if int(derivacao[1]) > contador:
				contador = int(derivacao[1])
				dictionary[palavra] = derivacao[0]	 
		else:
			contador = 0
			palavra = palavras[0]
			dictionary[palavra] = ''


	for topico_id, topico in enumerate(model.components_):
		mensagem = "Topico #%d: " % topico_id
		for i in topico.argsort()[:-n_top_words - 1:-1]:

			X = feature_names[i].split('_')
			cont_ruim = False
			palavra_completa = ""
			
			for palavra_separada in X:
				if cont_ruim:
					mensagem +="_"
				else:
					mensagem +=" "
					cont_ruim = True

				mensagem +=dictionary[palavra_separada]

		print (mensagem)


## Ler os arquivos que contem as tokens unicos
with open("palavras.txt", 'r') as f:
	palavras1 = []
	for line in f:
		line = line.strip('\n')
		palavras1.append(line)

#  Realizar o LDA de cada cluster separadamente primeiro
print("Realizando a modelagem de topicos LDA com tfidf features, " "n_documentos: %d e n_palavras = %d ..." % (n_samples, n_features))
lda = LatentDirichletAllocation(n_components = n_components, max_iter=5, learning_method='online', learning_offset=50., random_state=0)

j = 0
for k in clusterizacao:
	lda.fit(k)
	print('\nTopicos no Cluster_' + str(j) + ' modelo LDA:')
	j+=1
	tf_feature_names = palavras1
	print_top_words(lda, tf_feature_names, n_top_words)



