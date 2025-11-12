# Data Science Test Example
# Let's check that this still works

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
clean_energy_ch = pd.read_csv("/Users/ashleyedgar/Desktop/Ashley Edgar Data Science/ashley-edgar-data-science/03_Visualisation/Day 3/Exercises/renewable_power_plants_CH.csv")
clean_energy_ch.head()

st.write("Hello World")
st.write("New Change")
