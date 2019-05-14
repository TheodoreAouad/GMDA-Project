print("Importing libraries...")

import utils as u
import numpy as np
import pandas as pd
from compare_clusters import *

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

X = np.c_[X1.T,X2.T,X3.T,X4.T].T

c5 = u.get_kmeans_matrix(X,5)
c4 = u.get_kmeans_matrix(X,4)
c3 = u.get_kmeans_matrix(X,3)
c2 = u.get_kmeans_matrix(X,2)

emds_clusters = -1 + np.zeros((4,4))
clusterings = [c2,c3,c4,c5]
for i,c1 in enumerate(clusterings):
    for j,c2 in enumerate(clusterings):
        emds_clusters[i,j] = compare_clusters(c1,c2)
        
emds_clusters = pd.DataFrame(emds_clusters)
emds_clusters.to_csv('clusterings_times.csv')

print("csv file written.")