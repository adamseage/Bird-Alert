import os
import time
import ebird
import json

def update_data():
    # This function checks if the taxonomy_data.json file exists
    # and is older than 1 week. If so, it fetches new data from 
    # the eBird API and saves it to the file.
    update_taxonomy_data = True
    # Check existing taxonomy_data.json file and its age
    if os.path.exists("taxonomy_data.json"):
        age = time.time() - os.path.getmtime("taxonomy_data.json")
        if age < 604800:  # 1 week in seconds
            update_taxonomy_data = False
    # Write the taxonomy data to a JSON file if required
    if update_taxonomy_data:
        taxonomy_data = ebird.get_taxonomy_data()
        with open("taxonomy_data.json", "w") as f:
            json.dump(taxonomy_data, f, indent=4)
        print("Taxonomy data updated and saved to taxonomy_data.json")


def get_data():
    #check for existing taxonomy_data.json file and its age
    update_data()
    with open("taxonomy_data.json", "r") as f:
        taxonomy_data = json.load(f)
    return taxonomy_data

def get_species_common_names():
    taxonomy_data = get_data()
    common_names = [entry["comName"] for entry in taxonomy_data]
    return common_names

def get_species_code(species_name):
    taxonomy_data = get_data()
    for entry in taxonomy_data:
        if entry["comName"] == species_name:
            return entry["speciesCode"]
    return None

def  get_species_info(species_code):
    taxonomy_data = get_data()
    for entry in taxonomy_data:
        if entry["speciesCode"] == species_code:
            return entry
    return None