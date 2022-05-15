import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import math

def distance(point1, point2):
	return math.sqrt((point1[0]-point2[0])*(point1[0]-point2[0]) + (point1[1]-point2[1])*(point1[1]-point2[1]) + (point1[2]-point2[2])*(point1[2]-point2[2]))

img = plt.imread("pic.jpg")

width = img.shape[1]
height = img.shape[0]

img = img.reshape(width*height, 3)

for k in range(1,11):
	kmeans = KMeans(n_clusters=k, random_state=0).fit(img)
	labels = kmeans.labels_ 
	clusters  = kmeans.cluster_centers_

	error_value = 0
	for i in range(len(img)):
		error_value += distance(img[i], clusters[labels[i]])

	with open("chart_error.txt", "a") as file:
		file.write(str(int(error_value)))
		file.write("\n")

	with open("chart_clusters.txt", "a") as file:
		file.write(str(len(clusters)))
		file.write("\n")

	new_img = np.zeros_like(img)

	for i in range(len(new_img)):
		new_img[i] = clusters[labels[i]]

	img2 = new_img.reshape(height, width, 3)

with open("chart_error.txt", "r") as file:
	error = file.read().split("\n")

with open("chart_clusters.txt", "r") as file:
	clusters = file.read().split("\n")

error.pop()
clusters.pop()

for i in range(len(error)):
	error[i] = int(error[i])
	clusters[i] = int(clusters[i])

plt.plot(clusters, error)
plt.title('CHART')
plt.xlabel('CLUSTERS')
plt.ylabel('ERROR')
plt.show()