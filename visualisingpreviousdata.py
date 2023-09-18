import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (Replace 'Your_File_Path_Here.csv' with the actual path to your CSV file)
file_path = 'HPM09.20230918T210942.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(df.head())

# Check for missing values
missing_values = df.isnull().sum()
print("Missing Values:", missing_values)

# Remove rows with missing values
df_clean = df.dropna()

# Check the shape of the cleaned dataset
print("Shape of cleaned dataset:", df_clean.shape)

# Convert the 'Month' column to a datetime format
df_clean['Month'] = pd.to_datetime(df_clean['Month'].str.strip(), format='%Y %B')

# Sort the dataset by 'Month'
df_clean = df_clean.sort_values(by='Month')

# Exploratory Data Analysis (EDA)
# Plotting the time series of monthly percentage change in house prices
plt.figure(figsize=(16, 6))
sns.lineplot(x='Month', y='VALUE', data=df_clean)
plt.title('Monthly Percentage Change in Residential Property Prices in Dublin')
plt.xlabel('Month')
plt.ylabel('Percentage Change (%)')
plt.grid(True)
plt.show()
