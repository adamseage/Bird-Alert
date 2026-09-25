import taxonomy
import ebird
import state
import ui
import streamlit as st

def clear_results():
    st.session_state.sightings = []

state.setup_session_state()

ui.render_header()

ui.render_search_controls(taxonomy.get_species_common_names())

map_data = ui.render_map()

if map_data["last_clicked"] is not None:
    st.session_state.lat = map_data["last_clicked"]["lat"]
    st.session_state.lng = map_data["last_clicked"]["lng"]
    st.session_state.has_searched = False
  
    clear_results()
    st.rerun()

st.write(
    "Selected location:",
    st.session_state.lat,
    st.session_state.lng
)    

st.write("Bird:", st.session_state.bird)
st.write("Days:", st.session_state.days)
st.write("Search radius:", st.session_state.radius)

if st.button("Search"):
    clear_results()
    st.write(f"Searching for {st.session_state.bird} sightings in the last {st.session_state.days} days within a {st.session_state.radius} km radius...")
    species_code = taxonomy.get_species_code(st.session_state.bird)
    st.session_state.sightings = ebird.get_sightings(species_code=species_code,
                                        lat=st.session_state.lat,
                                        lng=st.session_state.lng,
                                        radius_km=st.session_state.radius,
                                        days_back=st.session_state.days)
    st.session_state.has_searched = True

if (len(st.session_state.sightings)==0) and st.session_state.has_searched:
    st.write("No sightings found for the selected bird in the specified time frame and radius.") 
elif not st.session_state.has_searched:
    st.write("Please select a bird and click 'Search' to find recent sightings.")
else:
    for sighting in st.session_state.sightings:
        st.write(f"Species: {sighting['comName']}, Location: {sighting['locName']}, Date: {sighting['obsDt']}")