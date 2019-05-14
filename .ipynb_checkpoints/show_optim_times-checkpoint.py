print("Importing libraries...")

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Imports successful")

ns = []
ms = []
times = []
with open('times_q4.csv',mode="r") as file:
    reader = csv.reader(file)
    for i,row in enumerate(reader):
        if i == 0:
            continue
        ns.append(row[0])
        ms.append(row[1])
        times.append(row[3])

ns = np.array(ns,dtype=float)
ms = np.array(ms,dtype=float)
times = np.array(times,dtype=float)

nxm = ns*ms
x = nxm[nxm.argsort()]
y = times[nxm.argsort()]
plt.plot(x,y,"o--")
plt.title("Time to compute the optimization problem")
plt.xlabel("m x n")
plt.ylabel("Time (s)")

plt.show()