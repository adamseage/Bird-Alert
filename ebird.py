import os
from urllib import response
import requests
import streamlit as st
from dotenv import load_dotenv, dotenv_values, 

def get_API_key():
    messages = [
        "API Pulled from streamlit secrets",
        "API not found in streamlit secrets, checking .env file",
        "API Pulled from environment variable",
        "NO API KEY FOUND, please add your eBird API key to the .env file or streamlit secrets",
    ]

    try:
        api_key = st.secrets["EBIRD_API_KEY"]
        if api_key:
            print(messages[0])
            return api_key
    except:
        print(messages[1])
        pass

    try:
        load_dotenv()
        api_key = os.getenv("EBIRD_API_KEY")
        if api_key:
            print(messages[2])
            return api_key
    except:
        print(messages[3])
        raise RuntimeError(messages[3])
    return api_key

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
    