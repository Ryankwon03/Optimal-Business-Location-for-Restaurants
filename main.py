import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os



df = pd.read_csv("Walmart.csv")

#print(df.head()) #checking data format
#print(df.isnull().sum()) #checking how many null values


print(df.describe())