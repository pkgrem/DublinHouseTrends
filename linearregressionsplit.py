import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the dataset
file_path = 'HPM09.20230918T210942.csv'
df = pd.read_csv(file_path)

# Remove rows with missing values
df_clean = df.dropna()

# Convert 'Month' to datetime and sort
df_clean['Month'] = pd.to_datetime(df_clean['Month'].str.strip(), format='%Y %B')
df_clean = df_clean.sort_values(by='Month')

# Create a time index variable
df_clean['Time_Index'] = np.arange(len(df_clean))

# Extract the year from the 'Month' column
df_clean['Year'] = df_clean['Month'].dt.year

# Split the data into two segments: before and after 2013
df_before_2013 = df_clean[df_clean['Year'] < 2013]
df_after_2013 = df_clean[df_clean['Year'] >= 2013]

# Fit Linear Regression models for each segment
# Before 2013
X_before = df_before_2013[['Time_Index']]
y_before = df_before_2013['VALUE']
lin_reg_before = LinearRegression()
lin_reg_before.fit(X_before, y_before)
y_pred_before = lin_reg_before.predict(X_before)

# After 2013
X_after = df_after_2013[['Time_Index']]
y_after = df_after_2013['VALUE']
lin_reg_after = LinearRegression()
lin_reg_after.fit(X_after, y_after)
y_pred_after = lin_reg_after.predict(X_after)

# Plot the segmented data and their linear trends
plt.figure(figsize=(16, 6))
plt.scatter(df_before_2013['Month'], y_before, label='Actual Data (Before 2013)', c='blue')
plt.plot(df_before_2013['Month'], y_pred_before, label='Linear Trend (Before 2013)', c='red')
plt.scatter(df_after_2013['Month'], y_after, label='Actual Data (After 2013)', c='green')
plt.plot(df_after_2013['Month'], y_pred_after, label='Linear Trend (After 2013)', c='orange')
plt.title('Segmented Monthly Percentage Change in Residential Property Prices in Dublin')
plt.xlabel('Month')
plt.ylabel('Percentage Change (%)')
plt.legend()
plt.grid(True)
plt.show()
