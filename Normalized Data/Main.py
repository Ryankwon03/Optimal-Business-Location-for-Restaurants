import pandas as pd
import numpy as np
import csv


df = pd.read_csv("Final_data.csv")
df = df.dropna()


print("What Country Restaurant?")
country_input = input()

final_dict = {}
cnt = 0

saved_zip = ""


for idx, row in df.iterrows():
    #고칠것: sort out top3 & worst3
    final_dict[row['ZipCode']] = round((row['/max - min(pop)']*0.262) + (float(row[country_input].strip("%"))*0.338) + (row['/max-min(employ)']*0.089) - (row['Normalized Crime Rates']*0.127) - (row['Normalized Competitors']*0.184), 2)
    
print(final_dict)