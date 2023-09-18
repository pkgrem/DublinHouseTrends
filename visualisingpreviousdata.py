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

# Breaking down the data into 3-year segments for trendlines
df_clean['Year'] = df_clean['Month'].dt.year
year_min = df_clean['Year'].min()
year_max = df_clean['Year'].max()

for start_year in range(year_min, year_max, 3):
    end_year = min(start_year + 3, year_max + 1)
    segment = df_clean[(df_clean['Year'] >= start_year) & (df_clean['Year'] < end_year)]
    if len(segment) > 1:
        z = np.polyfit(range(len(segment['Month'])), segment['VALUE'], 1)
        p = np.poly1d(z)
        plt.plot(segment['Month'], p(range(len(segment['Month']))), '--', label=f'Trend {start_year}-{end_year-1}')

plt.title('Monthly Percentage Change in Residential Property Prices in Dublin with Segmented Trendlines', fontsize=16)
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
