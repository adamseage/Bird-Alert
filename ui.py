import streamlit as st
import folium
from streamlit_folium import st_folium

def render_header():
    st.title("Bird Alert")
    st.write("Find recent bird sightings near your selected location.")

def render_search_controls(common_names):
    st.selectbox(
        "Bird",
        common_names,
        index=common_names.index("Sacred Kingfisher"),
        key="bird"
    )
    st.selectbox(
        "Days back",
        [1, 2, 3, 7, 14, 30],
        key="days"
    )
    st.slider(
        "Radius",
        1,
        50,
        key="radius"
    )
    return

def render_map():
    map_object = folium.Map(
        location=[
            st.session_state.lat,
            st.session_state.lng
        ],
        zoom_start=10
    )

    folium.Marker(
        location=[
            st.session_state.lat,
            st.session_state.lng
        ],
        tooltip="Search centre"
    ).add_to(map_object)

    folium.Circle(
        location=[
            st.session_state.lat,
            st.session_state.lng
        ],
        radius=st.session_state.radius * 1000,
        fill=True,
        fill_opacity=0.2
    ).add_to(map_object)

    map_data = st_folium(
        map_object,
        width=700,
        height=450
    )

    return map_data