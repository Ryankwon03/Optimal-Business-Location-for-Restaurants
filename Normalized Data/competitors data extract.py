import pandas as pd
import numpy as np
import csv

df = pd.read_csv("competitors.csv")

dictionary = {}


for i in df["zip_code"]:
    if(not (i in dictionary)):
        dictionary[i] = 1
    else:
        dictionary[i] = dictionary[i] + 1

print(dictionary)


    
    
with open('competitors_data.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames = ["ZipCode", "Count"])
    writer.writeheader()
    for key in dictionary.keys():
        f.write("%s, %s\n" % (key, dictionary[key]))
        