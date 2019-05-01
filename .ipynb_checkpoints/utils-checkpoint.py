import numpy as np

def generate_data(mean,std,size):
    dim = mean.shape[0]
    if np.array(std).shape == ():
        cov = np.eye(dim)*std
    else:
        cov = std
    X = np.random.multivariate_normal(mean=mean,cov=cov,size=(size))
    W = np.sum((X-mean)**2,1)
    return X,W