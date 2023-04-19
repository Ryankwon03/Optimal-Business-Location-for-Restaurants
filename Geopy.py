import geopy
from geopy.geocoders import Nominatim
import numpy as np
import pandas as pd
import csv

geolocator = Nominatim(user_agent="my_app")

zip_codes = {}

data = pd.read_csv("Crime_Data_from_2020_to_Present.csv")
latitude = []
longitude = []
for i in data:
    if(i == 'LAT'):
        for j in data[i]:
            latitude.append(j)
    if(i == 'LON'):
        for j in data[i]:
            longitude.append(j)
            
for i in range(len(latitude)):
    location = geolocator.reverse(f"{latitude[i]}, {longitude[i]}")
    address = location.raw['address']
    zipcode = address.get('postcode')
    
    if(zipcode not in zip_codes):
        zip_codes[zipcode] = 1
    else:
        zip_codes[zipcode] += 1
    print(zipcode, zip_codes[zipcode])
    
with open("cleaned_crime.csv", "w", newline="") as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)
    
    # Write the header row
    cnt = 0
    for key, value in zip_codes.items():
        print(cnt)
        writer.writerow([key, value])
        cnt = cnt + 1

    
    



print(zipcode)