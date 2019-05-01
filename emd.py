import numpy as np
from lp_solve import *
    
    
def EMD_prob(X1,W1,X2,W2,dist="euclid"):
    '''
    This function returns the EMD optimization problem in the following form:
    min d'x
    w.t. Ax <= b
    
    Args: 
    The two datasets we want to comput the EMD of, 
    X1: n x d array, points of the first dataset
    W1: n vector, weights of the first dataset
    X2: m x d array, points of the second dataset
    W2: m vector, weight of the second dataset
    
    Output:
    d: n*m vector, objective function
    A: n*m+n+m+2 x n*m array, inequality matrix of constraints
    b: n*m+n+m+2 vector, inequality vector of constraints
    '''
    
    n = X1.shape[0]
    m = X2.shape[0]
    D = np.zeros((n,m))
    
    if dist == "euclid":
        x1s = np.diag(X1@X1.T).reshape(n,1)
        x2s = np.diag(X2@X2.T).reshape(1,m)
        D = -2*X1@X2.T + x1s + x2s
    else:
        for i,x1 in enumerate(X1):
            for j,x2 in enumerate(X2):
                D[i,j] = dist(x1,x2)
    d = D.ravel()
    
    A1 = -np.eye(n*m)                      #constraints on direction of flow
    A2 = np.kron(np.eye(n),np.ones(m))     #constraints on weights of X1
    A3 = np.kron(np.ones(n),np.eye(m))     #constraints on weights of X2
    A4 = np.vstack([np.ones(n*m),-np.ones(n*m)])  #constraints on total flow
    
    b1 = np.zeros(n*m)
    b2 = W1
    b3 = W2
    b4 = min(W1.sum(),W2.sum()) + np.zeros(2)
    
    A = np.vstack((A1,A2,A3,A4))
    b = np.hstack((b1,b2,b3,b4))
    
    return d,A,b


def EMD(X1,W1,X2,W2,dist="euclid"):
    '''
    This function solves the EMD optimization problem.
    
    Args: 
    The two datasets we want to comput the EMD of, 
    X1: n x d array, points of the first dataset
    W1: n vector, weights of the first dataset
    X2: m x d array, points of the second dataset
    W2: m vector, weight of the second dataset
    
    Output:
    EMD: positive number, value of the EMD
    x: n*m vector, solution of the problem
    time: positive number, time taken to solve the problem
    '''
    n=X1.shape[0]
    m=X2.shape[0]
    d,A,b = EMD_prob(X1,W1,X2,W2,dist)
    [obj,x,duals,time] = lp_solve(d,A,b)
    emd = obj/min(W1.sum(),W2.sum())
    x = np.array(x).reshape(n,m)
    return [emd,x,time]