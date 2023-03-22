import numpy as np
import pandas as pd

df = pd.read_csv("tesla.csv")
movies = pd.read_csv("tmdb_5000_movies.csv")

print(df.head())
print(movies.head())
