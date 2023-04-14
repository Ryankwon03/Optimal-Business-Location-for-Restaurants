import requests
import numpy as np
import pandas as pd
import csv

def get_zipcode_from_lat_lng(latitude, longitude):
    api_key = "AIzaSyDeY_8ameEGTbi-yW2z3VEkiVhjyqObVEU" # Replace with your API key
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}"
    response = requests.get(url)
    json_data = response.json()
    for result in json_data['results']:
        for component in result['address_components']:
            if 'postal_code' in component['types']:
                return component['short_name']
    return None

if __name__ == "__main__":
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


# Open a new CSV file in write mode
x = [1, 2, 3, 4, 5, 6]
with open("cleaned_crime.csv", "w", newline="") as csvfile:
    
    # Create a CSV writer object
    writer = csv.writer(csvfile)
    
    # Write the header row
    writer.writerows(x)
    
            
            
    for i in range(len(latitude)):
        print(get_zipcode_from_lat_lng(latitude[i], longitude[i]))
        zip_codes[str(get_zipcode_from_lat_lng(latitude[i], longitude[i]))] = 0
    
    for i in range(len(latitude)):
        zip_codes[str(get_zipcode_from_lat_lng(latitude[i], longitude[i]))] += 1
    
    print(zip_codes)