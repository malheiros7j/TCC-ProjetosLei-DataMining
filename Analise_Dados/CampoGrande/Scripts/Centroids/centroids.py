from __future__ import print_function
import numpy as np 
import pandas as pd

from sklearn.preprocessing import Normalizer
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


n_clusters = 30
n_documentos = n_samples

clusterer = KMeans(n_clusters = n_clusters, init="k-means++")
cluster_labels = clusterer.fit_predict(date)


## Ler os arquivos que contem as tokens unicos
with open("palavras.txt", 'r') as f:
	palavras = []
	for line in f:
		line = line.strip('\n')
		palavras.append(line)


order_centroids = clusterer.cluster_centers_.argsort()[:, ::-1]
terms = palavras


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


for i in range(n_clusters):
	mensagem = "Cluster#%d: " % i
	for ind in order_centroids[i, :15]:

		X = terms[ind].split('_')
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



total = 0
for cluster in range(0, n_clusters):
	for index in range(0, n_documentos):
		if(cluster_labels[index] == cluster):
			total+=1

	porcentagem = 100.0 * total/n_documentos
	print("Cluster" +str(cluster)+ ":" +str(total) + " documentos, esse cluster representa: {0:.2f}".format(porcentagem)  + "% no total")
	total = 0
