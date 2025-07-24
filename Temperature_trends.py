#Understanding temperature variation within each months.
#Box plot!

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("weather_data.csv")


data['month'] = pd.to_datetime(data['Date_Time']).dt.month
sns.boxplot(x=data['month'], y=data['Wind_Speed_kmh'], palette="coolwarm")
plt.xlabel('Month')
plt.ylabel('Wind_Speed_kmh')
plt.title('Wind speed Variability by Month')
plt.show()


plt.savefig("Temperature_trends.py.png", dpi=300, bbox_inches='tight')

plt.show()
