import numpy as np
from emd import *


def compare_clusters(C1,C2,weights=None):
    '''
    This algorithm compares two clusters.
    Notations:
    k: number of clusters
    n: number of points
    
    Args:
    C1: k x n array, matrix of soft clustering
    C2: k x n array, matrix of soft clustering
    weights:  None OR tuple of two k vectors.
    If weights = None, the weights will be the sum of the coefficients for each cluster.
    
    Output:
    Earth Moving Distance
    '''
    
    def l1_dist(x1,x2):
        return np.sum(np.abs(x1-x2))
    
    if weights is None:
        W1,W2 = C1.sum(1)/C1.sum(),C2.sum(1)/C2.sum()
    else:
        W1,W2 = weights
    
    #assert W1.sum() == 1 and W2.sum() == 1, "Weights must sum to 1"
    emd,x,time = EMD(C1,W1,C2,W2,l1_dist)
    return emd