import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
data = pd.read_csv("weather_data.csv")

# Ensure data is numeric
data['Wind_Speed_kmh'] = pd.to_numeric(data['Wind_Speed_kmh'], errors='coerce')

# Aggregate in case of duplicate locations
data_grouped = data.groupby('Location', as_index=False)['Wind_Speed_kmh'].mean()

# Extract values
x = data_grouped['Location']
y = data_grouped['Wind_Speed_kmh']

# Create bar plot
plt.figure(figsize=(10, 5))
plt.bar(x, y, color='blue', edgecolor='green', linewidth=2)

# Improve readability
plt.title('Wind Speed by Location')
plt.xlabel('Location')
plt.ylabel('Wind Speed (km/h)')
plt.xticks(rotation=45, ha='right')  # Rotate labels for readability

plt.savefig("Bar.py.jpg", dpi=400, bbox_inches='tight')

plt.show()
