print("Importing libraries...")

import numpy as np
import pandas as pd
from tqdm import tqdm
import csv
from utils import *
from emd import *

print("Imports successful")

def compute_time():
    '''
    If the function stops prematurely, it is probably because there is
    too many points in the dataset.
    
    This function computes the time it takes to solve the optimization
    probleme for given sizes for n and m. It writes the times in a 
    csv file and in a pkl file.
    '''
    
    sigms = 1
    sigma1 = sigms
    sigma2 = sigms
    mean1 = np.array([1,1])
    mean2 = np.array([-1,-1])

    ns = np.array([50,60,70,90,110])
    ms = np.array([50,60,70,90,110])
    num_of_rep = 5

    objs = np.zeros((ns.shape[0],ms.shape[0]))
    times = np.zeros((ns.shape[0],ms.shape[0]))

    ns_gotten = set()
    ms_gotten = set()

    with open('times_q4.csv', mode='r') as file:
        reader = csv.reader(file)
        for i,row in enumerate(reader):
            if i == 0:
                continue
            ns_gotten.add(int(row[0]))
            ms_gotten.add(int(row[1]))


    for i in tqdm(range(ns.shape[0])):
        n=ns[i]
        for j,m in enumerate(ms):
            if m < n:
                continue
            if (n in ns_gotten) and (m in ms_gotten):
                continue
            X1,W1 = generate_data(mean1,sigma1,n)
            X2,W2 = generate_data(mean2,sigma2,m)

            current_obj = np.zeros(num_of_rep)
            current_time = np.zeros(num_of_rep)
            for k in range(num_of_rep):
                current_obj[k],_,current_time[k] = EMD(X1,W1,X2,W2)
            objs[i,j],times[i,j] = current_obj.mean(),current_time.mean()
            with open('times_q4.csv', mode='a',newline='') as file:
                writer = csv.writer(file)
                towrite = [n,m,mean1.shape[0],times[i,j],objs[i,j]]
                towrite = [str(k) for k in towrite]
                writer.writerow(towrite)

    timespd = pd.DataFrame(times,index=ns,columns=ms)
    timespd.to_pickle("time_q4.pkl")
    print("Matrix saved.")
    
compute_time()