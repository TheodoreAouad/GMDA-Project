import numpy as np
import pandas as pd
from utils import *
from emd import *

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

for i in tqdm(range(ns.shape[0])):
    n=ns[i]
    for j,m in enumerate(ms):
        if m < n:
            continue
        X1,W1 = generate_data(mean1,sigma1,n)
        X2,W2 = generate_data(mean2,sigma2,m)
        
        current_obj = np.zeros(num_of_rep)
        current_time = np.zeros(num_of_rep)
        for k in range(num_of_rep):
            current_obj[k],_,current_time[k] = EMD(X1,W1,X2,W2)
        objs[i,j],times[i,j] = current_obj.mean(),current_time.mean()
        
timespd = pd.DataFrame(times,index=ns,columns=ms)
timespd.to_pickle("time_q4.pkl")