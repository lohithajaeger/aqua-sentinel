import streamlit as st
import requests
import pandas as pd

st.title("Aqua Sentinel Lake Monitoring")

# fetch data from backend
try:
    data = requests.get("http://127.0.0.1:8000/data").json()
except:
    data = []

df = pd.DataFrame(data)

st.subheader("Sensor Data")

if len(df) > 0:

    st.dataframe(df)

    latest = df.iloc[-1]

    st.subheader("Latest Reading")

    st.write("Temperature:", latest["temperature"])
    st.write("pH:", latest["ph"])
    st.write("Oxygen:", latest["oxygen"])

    if latest["oxygen"] < 200:
        st.error("⚠ Algal Bloom Risk")
    else:
        st.success("Water Safe")

else:
    st.write("No sensor data received yet.")