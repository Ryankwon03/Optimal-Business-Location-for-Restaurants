import requests
import numpy as np
import pandas as pd

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
    data = pd.read_csv("Crime_Data_from_2020_to_Present.csv")
    print(data.head())
    for i in data:
        
