from __future__ import print_function
import numpy as np 
import pandas as pd

import matplotlib.pyplot as plt
import sys
import copy

from sklearn.preprocessing import Normalizer
from sklearn.decomposition import LatentDirichletAllocation


from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster


data = pd.read_csv("manaus.csv")
data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)
data.drop(data.columns[0], axis = 1, inplace = True)

n_samples, n_features = data.shape

# Normalizacao dos Dados
normalizer = Normalizer(copy=False)
date = normalizer.fit_transform(data)


print("n_documentos:%d \t n_palavras: %d \t " % (n_samples, n_features))
print(82 * '_')
print('\n')

np.set_printoptions(precision=4,suppress=True)
plt.figure(figsize=(10,3))
plt.style.use('seaborn-whitegrid')


# Realiza a linkagem para A clusterizacao hierarquica

z = linkage(date, method='ward', metric='euclidean')
# Dendrograma
dendrogram(z, truncate_mode="lastp", p=30,orientation='top', show_contracted=False, no_labels=True)

plt.show()

k = 30
cluster_labels = fcluster(z, k, criterion="maxclust")
# print cluster_labels

'''
orig_stdout = sys.stdout
f = open('clusters_labels.txt', 'w')
sys.stdout = f

for x in cluster_labels:
    print x

sys.stdout = orig_stdout
f.close()
'''

'''
##### Criar uma lista de clusters ##### 
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
cluster15 = []
cluster16 = []
cluster17 = []
cluster18 = []
cluster19 = []
cluster20 = []
cluster21 = []
cluster22 = []
cluster23 = []
cluster24 = []
cluster25 = []
cluster26 = []
cluster27 = []
cluster28 = []
cluster29 = []
cluster30 = []

for i in range(len(cluster_labels)):

	if cluster_labels[i] == 1:
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
	elif cluster_labels[i] == 15:
		cluster15.append(date[i])
	elif cluster_labels[i] == 16:
		cluster16.append(date[i])
	elif cluster_labels[i] == 17:
		cluster17.append(date[i])
	elif cluster_labels[i] == 18:
		cluster18.append(date[i])
	elif cluster_labels[i] == 19:
		cluster19.append(date[i])
	elif cluster_labels[i] == 20:
		cluster20.append(date[i])
	elif cluster_labels[i] == 21:
		cluster21.append(date[i])
	elif cluster_labels[i] == 22:
		cluster22.append(date[i])
	elif cluster_labels[i] == 23:
		cluster23.append(date[i])
	elif cluster_labels[i] == 24:
		cluster24.append(date[i])
	elif cluster_labels[i] == 25:
		cluster25.append(date[i])
	elif cluster_labels[i] == 26:
		cluster26.append(date[i])
	elif cluster_labels[i] == 27:
		cluster27.append(date[i])
	elif cluster_labels[i] == 28:
		cluster28.append(date[i])
	elif cluster_labels[i] == 29:
		cluster29.append(date[i])
	elif cluster_labels[i] == 30:
		cluster30.append(date[i])

## Roxo
cluster29_30 = cluster29 + cluster30
cluster28_30 = cluster28 + cluster29_30


## Azul Claro
cluster26_27 = cluster26 + cluster27
cluster24_25 = cluster24 + cluster25
cluster24_27 = cluster24_25 + cluster26_27
cluster22_23 = cluster22 + cluster23 
cluster22_27 = cluster22_23  + cluster24_27
cluster22_30 = cluster22_27 + cluster28_30


cluster21_30 = cluster21 + cluster22_30

cluster19_20 = cluster19 + cluster20 
cluster19_30 = cluster19_20 + cluster21_30

cluster17_18 = cluster17 + cluster18
cluster17_30 = cluster17_18 + cluster19_30
cluster16_30 = cluster16 + cluster17_30
cluster15_30 = cluster15 + cluster16_30

cluster13_14 = cluster13 + cluster14
cluster12_14 = cluster12 + cluster13_14
cluster11_14 = cluster11 + cluster12_14
cluster10_14 = cluster10 + cluster11_14

cluster10_30 = cluster10_14 + cluster15_30

cluster9_30 = cluster9 + cluster10_30


cluster7_8 = cluster7 + cluster8 
cluster5_6 = cluster5 + cluster6 
cluster4_6 = cluster4 + cluster5_6
cluster4_8 = cluster4_6 + cluster7_8

cluster3_8 = cluster3 + cluster4_8

cluster3_30 = cluster3_8 + cluster9_30

cluster2_30 = cluster2 + cluster3_30
cluster1_30 = cluster1 + cluster2_30



clusterizacao = [cluster1, cluster2, cluster3, cluster4,cluster5, cluster6, cluster7, cluster8,cluster9, cluster10, cluster11, cluster12,cluster13, cluster14, cluster15,
cluster16, cluster17,cluster18,cluster19,cluster20,cluster21,cluster22,cluster23,cluster24,cluster25,cluster26,cluster27,cluster28,cluster29,cluster30]

clusterizacao1 = [cluster29_30,cluster28_30,cluster26_27,cluster24_25,cluster24_27,cluster22_23,cluster22_27,cluster22_30,cluster21_30,cluster19_20,cluster19_30,cluster17_18,cluster17_30,cluster16_30,
cluster15_30,cluster13_14,cluster12_14,cluster11_14,cluster10_14,cluster10_30,cluster9_30,cluster7_8,cluster5_6,cluster4_6,cluster4_8,cluster3_8,cluster3_30,cluster2_30,cluster1_30]


n_components = 5
n_top_words = 10

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

j = 1
for k in clusterizacao:
	lda.fit(k)
	print('\nTopicos no Cluster_' + str(j) + ' modelo LDA:', len(k))
	j+=1
	tf_feature_names = palavras1
	print_top_words(lda, tf_feature_names, n_top_words)

print('\n')
print('\n')


p = 1
for a in clusterizacao1:
	lda.fit(a)
	print('\nTopicos no Cluster_' + str(p) + ' modelo LDA:', len(a))
	p+=1
	tf_feature_names = palavras1
	print_top_words(lda, tf_feature_names, n_top_words)'''
