import pandas as pd

# Load the dataset
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
