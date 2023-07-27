import time 

start_time = time.time()

import pandas as pd

 
data = pd.read_csv("dataset.csv")

print(data.info())
print(data.head())
print(data.corr())

print("\n")

print(time.time() - start_time,"seconds to run program on pypy.")
