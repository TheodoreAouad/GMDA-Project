import numpy as np
from sklearn.cluster import KMeans

def generate_data(mean,std,size):
    dim = mean.shape[0]
    if np.array(std).shape == ():
        cov = np.eye(dim)*std
    else:
        cov = std
    X = np.random.multivariate_normal(mean=mean,cov=cov,size=(size))
    W = np.sum((X-mean)**2,1)
    return X,W

def get_kmeans_matrix(X,k):
    '''
    This function takes as input some data and a number of clusters, and returns a matrix cluster.
    
    Args:
    X: n x d array, array of data
    k: int, number of clusters
    
    Output:
    c : k x n matrix, c_ij = 1 if point j in cluster i, 0 otherwise 
    '''
    
    n = X.shape[0]
    c = np.zeros((n,k))
    kmeans = KMeans(n_clusters=k,init="random")
    clusters = kmeans.fit_predict(X)
    c[np.arange(n),clusters]=1
    return c.T
    
def write_lpfile(f,A,B,option="min",name="to_solve"):
    '''
    Write the .lp file to put in the lp_solve.
    Solves:
    min/max <x,f>
    w.t. Ax <= B
    '''
    
    n = f.shape[0]-1
    file = open(name+".lp","w")
    #Write the objective function
    file.write("/* Objective function */\n")
    file.write(option+": ")
    towrite = []
    for idx,k in enumerate(f):
        if k != 0:
            towrite.append(str(k)+"x"+str(idx))
        
    towrite = " + ".join(towrite) + ";\n"
    file.write(towrite)
    file.write("\n")
    
    #Write the variable bounds
    file.write("/* Variable bounds */\n")
    for a,b in zip(A,B):
        towrite = []
        for idx,k in enumerate(a):
            if k != 0:
                towrite.append(str(k)+"x"+str(idx))
        towrite = " + ".join(towrite) + " <= " + str(b) + ";\n"
        file.write(towrite)
    file.close()