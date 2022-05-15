import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import math

def distance(point1, point2):
	return math.sqrt((point1[0]-point2[0])*(point1[0]-point2[0]) + (point1[1]-point2[1])*(point1[1]-point2[1]) + (point1[2]-point2[2])*(point1[2]-point2[2]))

img = plt.imread("pic1.jpg")

width = img.shape[1]
height = img.shape[0]

img = img.reshape(width*height, 3)

# print(img.shape)
kmeans = KMeans(n_clusters=4, random_state=0).fit(img)
labels = kmeans.labels_ 
clusters  = kmeans.cluster_centers_

error_value = 0
for i in range(len(img)):
	error_value += distance(img[i], clusters[labels[i]])

# print(error_value)

# print(len(clusters))

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

plt.imshow(img2)
plt.show()