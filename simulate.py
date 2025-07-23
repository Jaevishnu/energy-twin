import pandas as pd
import numpy as np

def generate_energy_data():
    np.random.seed(42)
    time = pd.date_range(start='9:00', periods=10, freq='H')
    temperature = np.random.normal(24, 2, size=10)
    energy = np.random.normal(4, 1, size=10)
    occupancy = np.random.choice([0, 1], size=10, p=[0.3, 0.7])
    return pd.DataFrame({
        "Time": time,
        "Room Temp (°C)": temperature,
        "Energy Used (kWh)": energy,
        "Occupancy": occupancy
    })
