import pandas as pd

df1 = pd.read_csv('Normalized Crime Data.csv')
df2 = pd.read_csv('Normalized Population.csv')
df3 = pd.read_csv('normalized_la_employment.csv')

# Merge the dataframes based on the "ZipCodes" column
merged_df = pd.merge(df1, df2, on='ZipCode')
merged_df = pd.merge(merged_df, df3, on='ZipCode')

# Save the merged dataframe as a CSV file
merged_df.to_csv('Final_Data.csv', index=False)
