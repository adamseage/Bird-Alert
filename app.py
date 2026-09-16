import streamlit as st
import os
import requests 
from dotenv import load_dotenv, dotenv_values 

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv("EBIRD_API_KEY")

def species_code_from_name(bird_name):
    bird_species_codes = {
        "Sacred Kingfisher": "sackin1",
        "Laughing Kookaburra": "lauk",
        "Rainbow Lorikeet": "ralo",
    }
    return bird_species_codes.get(bird_name, None)

def get_sightings(species_code, lat, lng, radius_km, days_back, API_KEY=API_KEY):
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
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching data from eBird API: {response.status_code}")
        return []



st.title("Bird Alert")
st.write("Welcome to Bird Alert! This app helps you identify birds based on their characteristics and sounds. Please enter the details of the bird you want to identify below.")

bird = st.selectbox(
    "Select the bird you wish to target",
    [
        "Sacred Kingfisher",
        "Laughing Kookaburra",
        "Rainbow Lorikeet",
    ]
)
days = st.selectbox(
    "Days back to search for sightings",
    [1, 2, 3, 7, 14, 30],
)
radius = st.selectbox(
    "Select the search radius in kilometers",
    [1, 5, 10, 20, 50],
)



st.write("Bird:", bird)
st.write("Days:", days)
st.write("Search radius:", radius)

if st.button("Search"):
    st.write(f"Searching for {bird} sightings in the last {days} days within a {radius} km radius...")
    
    species_code = species_code_from_name(bird)
    sightings = get_sightings(species_code=species_code, lat=-33.8688, lng=151.2093, radius_km=radius, days_back=days)
    for sighting in sightings:
        st.write(f"Species: {sighting['comName']}, Location: {sighting['locName']}, Date: {sighting['obsDt']}")    
