import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("weather_data.csv")

plot = sns.FacetGrid(data, col="Temperature")
plot.map(plt.plot, "Date_Time")

plt.show()
