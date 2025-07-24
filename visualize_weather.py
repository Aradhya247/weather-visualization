import matplotlib.pyplot as plt
import pandas as pd

# Load weather data
data = pd.read_csv("weather_data.csv")

# Plot temperature vs. humidity
plt.scatter(data['Precipitation_mm'], data['Wind_Speed_kmh'], alpha=0.5)
plt.xlabel('Precipitation_mm')
plt.ylabel('Wind_Speed_kmh')
plt.title('Precipitation vs Wind speed')
plt.show()


plt.savefig("visualize_weather.py.png", dpi=300, bbox_inches='tight')

plt.show()