import numpy as np
import pandas as pd

df = pd.read_csv("walmart.csv")

print(df.head())

print(df[0:2].T)