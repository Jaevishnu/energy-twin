import streamlit as st
import pandas as pd
import numpy as np
from simulate import generate_energy_data
from suggestions import suggest_optimizations

st.set_page_config(page_title="SmartClass Energy Twin", layout="wide")
st.title("🏫 SmartClass Energy Twin Dashboard")

df = generate_energy_data()
st.line_chart(df[["Room Temp (°C)", "Energy Used (kWh)"]])

st.subheader("💡 AI Suggestions for Energy Optimization")
suggestions = suggest_optimizations(df)
for s in suggestions:
    st.warning(s)
