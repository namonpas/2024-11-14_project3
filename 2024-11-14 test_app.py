import streamlit as st
import plotly.express as px
import pandas as pd


st.title('My First Streamlit App')


# Sample data
data = pd.DataFrame({
    'city': ['Bangkok', 'Chiang Mai', 'Phuket'],
    'lat': [13.7563, 18.7883, 7.8804],
    'lon': [100.5018, 98.9867, 98.3984]
})

# Create a Plotly map with interactive pan and zoom
fig = px.scatter_mapbox(data, lat="lat", lon="lon", hover_name="city",
                        color_discrete_sequence=["fuchsia"], zoom=5)
fig.update_layout(mapbox_style="open-street-map")
st.plotly_chart(fig)
