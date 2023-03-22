import pandas as pd

df = pd.read_csv("tesla.csv")
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

print(df.head())
print(movies.head())
print(credits.head())