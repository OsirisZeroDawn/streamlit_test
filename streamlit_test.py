
# Streamlit live coding script
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy

#Data from: https://data.open-power-system-data.org/renewable_power_plants/

st.write("This is my streamlit Application - Visualizating Green Energy Locations in Switzerland")
st.write("New Change")

clean_energy_ch = pd.read_csv("https://data.open-power-system-data.org/renewable_power_plants/2020-08-25/renewable_power_plants_CH.csv")
clean_energy_ch.head()

st.write("This is a Data Frame with all our Data:")
st.write(clean_energy_ch)
