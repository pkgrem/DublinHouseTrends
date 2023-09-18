import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

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
sns.lineplot(x='Month', y='VALUE', data=df_clean, color='royalblue')
plt.title('Monthly Percentage Change in Residential Property Prices in Dublin', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Percentage Change (%)', fontsize=14)

# Improve x-axis formatting and ticks
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gcf().autofmt_xdate()

# Highlight important points or ranges (if any)
# Example: Highlighting a year range
# plt.axvspan('2020-01', '2021-01', color='grey', alpha=0.2, label='Year Range of Interest')

# Add grid and legend
plt.grid(True)
# plt.legend()

# Show plot
plt.show()
