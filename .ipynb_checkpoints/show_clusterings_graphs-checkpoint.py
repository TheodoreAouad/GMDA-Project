print("Importing libraries...")

import utils as u
import numpy as np
import matplotlib.pyplot as plt

print("Imports successful")


mean1 = np.array([1,1])
mean2 = np.array([-1,-5])
mean3 = np.array([1,-5])
mean4 = np.array([-1,1])

std = 0.2
std1 =std
std2 = std
std3 = std
std4 = std

size = 200

X1,_ = u.generate_data(mean=mean1,std=std1,size=size)
X2,_ = u.generate_data(mean=mean2,std=std2,size=size)
X3,_ = u.generate_data(mean=mean3,std=std3,size=size)
X4,_ = u.generate_data(mean=mean4,std=std4,size=size)

Y1 = np.zeros(size)+1
Y2 = np.zeros(size)+2
Y3 = np.zeros(size)+3
Y4 = np.zeros(size)+4

X = np.c_[X1.T,X2.T,X3.T,X4.T].T
Y = np.c_[Y1.T,Y2.T,Y3.T,Y4.T].T.reshape(4*size)
plt.scatter(X[:,0],X[:,1],c=Y)


c5 = u.get_kmeans_matrix(X,5)
c4 = u.get_kmeans_matrix(X,4)
c3 = u.get_kmeans_matrix(X,3)
c2 = u.get_kmeans_matrix(X,2)

plt.figure(figsize = (20,20))
plt.subplot(221)
plt.title("2 clusters")
plt.scatter(X[:,0],X[:,1],c=c2.argmax(0))
plt.subplot(222)
plt.title("3 clusters")
plt.scatter(X[:,0],X[:,1],c=c3.argmax(0))
plt.subplot(223)
plt.title("4 clusters")
plt.scatter(X[:,0],X[:,1],c=c4.argmax(0))
plt.subplot(224)
plt.title("5 clusters")
plt.scatter(X[:,0],X[:,1],c=c5.argmax(0))

plt.show()