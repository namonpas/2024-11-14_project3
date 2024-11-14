import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Configuration for desktop display
st.set_page_config(
    page_title="Thailand Map Explorer",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# Custom CSS for better desktop fit
st.markdown("""
    <style>
        .main > div {
            padding-top: 0.5rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        .stSidebar > div {
            padding-top: 1.5rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        [data-testid="stSidebar"] {
            min-width: 220px !important;
            max-width: 220px !important;
        }
        .title-text {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        .metric-card {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 0.5rem;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar filters
with st.sidebar:
    st.markdown('<p class="title-text">Filters</p>', unsafe_allow_html=True)
    
    data_type = st.selectbox(
        "Data Type",
        ["Multiple values", "Single value", "Aggregated"],
        key="data_type"
    )
    
    view_by = st.selectbox(
        "View by",
        ["Tambon", "Amphoe", "Province"],
        key="view_by"
    )
    
    time_period = st.select_slider(
        "Time Period",
        options=["1M", "3M", "6M", "1Y", "All"],
        value="3M"
    )
    
    # Additional filters
    st.markdown("### Performance Threshold")
    min_performance = st.slider("Minimum Performance (%)", 0, 100, 50)
    
    # Region selection
    regions = ["All Regions", "Northern", "Central", "Eastern", "Southern"]
    selected_region = st.multiselect("Select Regions", regions, default="All Regions")
    
    st.markdown("---")
    if st.button("Apply Filters", use_container_width=True):
        st.success("Filters applied successfully!")

# Main content
st.markdown('<p class="title-text">Model Performance by Region</p>', unsafe_allow_html=True)

# Create two columns for the main content
col1, col2 = st.columns([7, 3])

with col1:
    # Function to create the Thailand map
    def create_thailand_map(data=None):
        thailand_center = [13.7563, 100.5018]
        m = folium.Map(
            location=thailand_center,
            zoom_start=6,
            tiles='CartoDB positron'
        )
        
        # Add custom map controls
        folium.LayerControl().add_to(m)
        
        return m
    
    # Create and display the map
    m = create_thailand_map()
    st_folium(
        m,
        width=None,
        height=500,
        returned_objects=["last_active_drawing", "last_clicked"]
    )

with col2:
    st.markdown("### Region Statistics")
    # Add some example metrics in cards
    st.markdown("""
        <div class="metric-card">
            <h4>Overall Performance</h4>
            <h2>78.5%</h2>
            <p style="color: green;">↑ 2.1% from last period</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Top Performing Areas")
    performance_data = pd.DataFrame({
        'Region': ['Chiang Mai', 'Bangkok', 'Phuket'],
        'Performance': ['96%', '94%', '92%']
    })
    st.table(performance_data)

# Bottom metrics section
st.markdown("---")
metric_cols = st.columns(4)
with metric_cols[0]:
    st.markdown("""
        <div class="metric-card">
            <h4>Total Regions</h4>
            <h2>77</h2>
        </div>
    """, unsafe_allow_html=True)
with metric_cols[1]:
    st.markdown("""
        <div class="metric-card">
            <h4>Above Target</h4>
            <h2>23</h2>
            <p style="color: green;">↑ 3 from last month</p>
        </div>
    """, unsafe_allow_html=True)
with metric_cols[2]:
    st.markdown("""
        <div class="metric-card">
            <h4>Below Target</h4>
            <h2>12</h2>
            <p style="color: red;">↓ 2 from last month</p>
        </div>
    """, unsafe_allow_html=True)
with metric_cols[3]:
    st.markdown("""
        <div class="metric-card">
            <h4>Data Coverage</h4>
            <h2>94.2%</h2>
        </div>
    """, unsafe_allow_html=True)