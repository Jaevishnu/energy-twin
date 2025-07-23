def suggest_optimizations(df):
    suggestions = []
    for _, row in df.iterrows():
        if row["Occupancy"] == 0 and row["Energy Used (kWh)"] > 3.5:
            suggestions.append("⚠️ Energy used while room is empty. Consider turning off devices.")
        if row["Room Temp (°C)"] < 20 or row["Room Temp (°C)"] > 26:
            suggestions.append("🌡️ Room temperature outside comfort range. Adjust HVAC settings.")
    return suggestions
