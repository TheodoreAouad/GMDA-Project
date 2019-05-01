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