import pandas as pd
import csv

df1 = pd.read_csv('Normalized Crime Data.csv')
df2 = pd.read_csv('Normalized Population.csv')
df3 = pd.read_csv('normalized_la_employment.csv')
df4 = pd.read_csv('competitors_data.csv')

# Merge the dataframes based on the "ZipCodes" column
final_df = pd.merge(df2, df3, how = "outer")

df4['ZipCode']=df4['ZipCode'].astype(int)

final_df = pd.merge(final_df, df4, how = "outer")

final_df['ZipCode']=final_df['ZipCode'].astype(str)
final_df = pd.merge(df1, final_df, how = "outer")

print(final_df)

final_df.to_csv('Final_data.csv')