#Module used to get the time in seconds
import time 
start_time = time.time()
#Module used for data processing
import pandas as pd
#importing the dataset
data = pd.read_csv("dataset.csv")
#displaying the details, first few columns and correlation
print(data.info())
print(data.head())
print(data.corr())
print("\n")
#displaying the time taken for the program to run
print(time.time() - start_time,"seconds to run program on pypy.")
