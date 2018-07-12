import matplotlib.pyplot as plt


x = []
y = []

dataset = open('1-StdDev.txt', 'r')

for line in dataset:

	line = line.strip()
	X, Y = line.split()
	x.append(X)
	y.append(Y)


dataset.close()

plt.plot(x,y)

plt.title('Analise de Corte')
plt.xlabel('Token correspondente')
plt.ylabel('Frequencia das Palavras')


plt.show()
