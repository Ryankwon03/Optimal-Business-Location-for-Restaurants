import pandas as pd
import numpy as np
import csv


data = pd.read_csv("la_population.csv")
print(data)

population = []
for i in data.keys():
    if(i == "Total Population, All Races"):
        for j in data[i]:
            population.append(j)


for i in range(len(population)):
    population[i] = int(population[i].replace(",", "")) 
    print(population[i])



for i in data.keys():
    if(i != "Total Population, All Races") and (i[0] != "Z"):
        for j in range(len(population)):
            if('0' <= data[i][j][0] <= '9'):
                data[i][j] = round(float(data[i][j][:-1]) * population[j] / 100.0)

print(data)

data.to_csv("race_convert.csv", index=False)

            
            #data[i][j] = float(data[i][j][:-1]) * population[j] / 100.0



#print(data)
#float(population) * float(percentage) / 100
