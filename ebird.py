import os
from urllib import response
import requests 
from dotenv import load_dotenv, dotenv_values 

def get_API_key():
    load_dotenv()  # Load environment variables from .env file
    return os.getenv("EBIRD_API_KEY")

def get_taxonomy_data():
    API_KEY = get_API_key()
    url = "https://api.ebird.org/v2/ref/taxonomy/ebird"
    headers = {
        "X-eBirdApiToken": API_KEY
    }
    response = requests.get(
        url, headers=headers,
        params={"fmt": "json"},
        timeout=10,
    )
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def get_sightings(species_code, lat, lng, radius_km, days_back):
    API_KEY = get_API_key()
    url = f"https://api.ebird.org/v2/data/obs/geo/recent/{species_code}"
    headers = {
        "X-eBirdApiToken": API_KEY
    }
    response = requests.get(
        url, headers=headers,
        params={"lat": lat,
                "lng": lng,
                "dist": radius_km,
                "back": days_back},
        timeout=10,
    )
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()
    