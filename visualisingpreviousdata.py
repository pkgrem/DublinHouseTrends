import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
import numpy as np

# Set a seaborn style for better aesthetics
sns.set(style="whitegrid")

# Load the dataset 
file_path = 'HPM09.20230918T210942.csv'
df = pd.read_csv(file_path)

# Remove rows with missing values
df_clean = df.dropna()

# Convert 'Month' to datetime and sort
df_clean['Month'] = pd.to_datetime(df_clean['Month'].str.strip(), format='%Y %B')
df_clean = df_clean.sort_values(by='Month')

# Plotting
plt.figure(figsize=(16, 6))
sns.lineplot(x='Month', y='VALUE', data=df_clean, color='royalblue', label='Monthly Change')

# Add a trendline using numpy's polyfit
z = np.polyfit(range(len(df_clean['Month'])), df_clean['VALUE'], 1)
p = np.poly1d(z)
plt.plot(df_clean['Month'], p(range(len(df_clean['Month']))), 'r--', label='Trendline')

plt.title('Monthly Percentage Change in Residential Property Prices in Dublin with Trendline', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Percentage Change (%)', fontsize=14)

# Improve x-axis formatting and ticks
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gcf().autofmt_xdate()

# Add grid and legend
plt.grid(True)
plt.legend()

# Show plot
plt.show()
