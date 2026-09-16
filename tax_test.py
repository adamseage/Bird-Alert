import os
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv("EBIRD_API_KEY")

def get_taxonomy_data():
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
    taxonomy_data = response.json()
    return taxonomy_data

# Check existance of taxonomy_data.json file
updated = False
if os.path.exists("taxonomy_data.json"):
    age = time.time() - os.path.getctime("taxonomy_data.json")
    print(f"taxonomy_data.json file exists. and has age: {age:.2f} seconds")
    if age > 604800:  # 1 week in seconds
        print("taxonomy_data.json is older than one week. Updating...")
        updated = True
    else:
        print("taxonomy_data.json is up to date.")
else:
    print("taxonomy_data.json file does not exist. Creating...")
    updated = True

# Write the taxonomy data to a JSON file
if updated:
    taxonomy_data = get_taxonomy_data()
    with open("taxonomy_data.json", "w") as f:
        json.dump(taxonomy_data, f, indent=4)

#print(type(taxonomy_data))
#print(len(taxonomy_data))
#print(taxonomy_data[0])  # Print the first entry to see its structure

