import pandas as pd

# Assuming your CSV file is named 'your-file.csv'
file_path = 'framingham.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Now 'df' contains your data, and you can perform operations on it
print(df.head(10))