import os
import requests 
from dotenv import load_dotenv, dotenv_values 

# loading variables from .env file
load_dotenv() 

API_KEY = os.getenv("EBIRD_API_KEY")

species_code = "sackin1" # Example species code for Sacred Kingfisher

lat = -33.8688 # Example latitude
lng = 151.2093 # Example longitude
radius_km = 25
days_back = 7

url = f"https://api.ebird.org/v2/data/obs/geo/recent/{species_code}?lat={lat}&lng={lng}&dist={radius_km}&back={days_back}"

params = {
    "lat": lat,
    "lng": lng,
    "dist": radius_km,
    "back": days_back
}

headers = {
    "X-eBirdApiToken": API_KEY
}

response = requests.get(url, headers=headers, params=params)

print("HTTP status:", response.status_code)
data = response.json()
for sighting in data:
    print(f"Species: {sighting['comName']}, Location: {sighting['locName']}, Date: {sighting['obsDt']}")    

print(response.url)