print("Importing libraries ...")

import argparse
import pandas as pd
from emd import EMD_prob
from utils import write_lpfile

print("Imports successful")

parser = argparse.ArgumentParser(description="Paths to csv data1, csv data2")
parser.add_argument('csv1',type=str,help="Path to first dataset")
parser.add_argument('csv2',type=str,help="Path to second dataset")

args = parser.parse_args()

D1 = pd.read_csv(args.csv1).values
D2 = pd.read_csv(args.csv2).values

X1,W1 = D1[:,:-1], D1[:,-1]
X2,W2 = D2[:,:-1], D2[:,-1]

d,A,b = EMD_prob(X1,W1,X2,W2)
write_lpfile(d,A,b)
print(".lp file written.")