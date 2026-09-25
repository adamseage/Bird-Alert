import streamlit as st

def setup_session_state():
    defaults = {
        "lat": -33.8688,
        "lng": 151.2093,
        "radius": 20,
        "sightings": [],
        "has_searched": False,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def clear_results():
    st.session_state.sightings = []