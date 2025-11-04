import streamlit as st
import random
import time
from collections import deque
import streamlit as st
# Custom CSS for better design
st.markdown("""
    <style>
    .alert-box {
        background-color: #fff3cd;
        color: #856404;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 12px;
        font-weight: bold;
        border-left: 6px solid #ffcc00;
    }
    </style>
""", unsafe_allow_html=True)

# Page title and subtitle with college name
st.set_page_config(page_title="Air Quality Monitoring", page_icon="🌍", layout="wide")

st.markdown("""
    <h1 style="text-align: center; color: #4CAF50;">
        🌍 Real-Time Air Quality Monitoring System
    </h1>
    <h4 style="text-align: center; color: #D3D3D3;">
        Velalar College of Engineering and Technology
    </h4>
    <hr>
""", unsafe_allow_html=True)

# Title and description
st.title("🌍 Real-Time Air Quality Monitoring System")
st.write("Using *Queue + Hash Map* to simulate live air quality readings.")

# Initialize queue and hash map
sensor_queue = deque()
pollutants = {"PM2.5": 0, "CO2": 0, "NO2": 0, "O3": 0}

# Threshold values for alerts
thresholds = {"PM2.5": 100, "CO2": 1200, "NO2": 80, "O3": 100}

# Streamlit placeholder for live updates
placeholder = st.empty()

# Store historical readings for visualization
history = {"PM2.5": [], "CO2": [], "NO2": [], "O3": []}

# Simulate real-time data for 20 readings
for i in range(20):
    # Generate random sensor data
    reading = {
        "PM2.5": random.randint(50, 150),
        "CO2": random.randint(800, 1600),
        "NO2": random.randint(40, 100),
        "O3": random.randint(60, 120)
    }

    # Enqueue the reading
    sensor_queue.append(reading)

    # Dequeue and process the oldest reading
    if len(sensor_queue) > 5:  # keep only last 5 readings
        sensor_queue.popleft()

    # Update latest readings in the hash map
    for key, value in reading.items():
        pollutants[key] = value
        history[key].append(value)

    # Display in Streamlit
    with placeholder.container():
        st.subheader("📊 Current Air Quality Readings")
        st.json(pollutants)

        # Show alert if threshold exceeded
        for key, value in pollutants.items():
            if value > thresholds[key]:
                st.warning(f"⚠ ALERT: {key} level is HIGH ({value})!")

        # Plot pollutant trends
        st.line_chart(history)

        st.caption(f"Updated {i+1} times...")

    time.sleep(1)

st.success("✅ Monitoring Complete!")