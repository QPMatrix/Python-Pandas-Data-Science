import pandas as pd

# Load data from different file formats
df_csv = pd.read_csv('./pokemon_data.csv')
df_xlsx = pd.read_excel('./pokemon_data.xlsx')
df_txt = pd.read_csv('./pokemon_data.txt', delimiter='\t')

# Reading Headers
print("Reading Headers:")
print("CSV file columns:\n", df_csv.columns)
print("\nXLSX file columns:\n", df_xlsx.columns)
print("\nTXT file columns:\n", df_txt.columns)

# Reading specific columns
print("\nReading specific columns:")

# Get the first 5 indexes of the 'Name' column from the CSV file
print("\nFirst 5 names from CSV file:\n", df_csv['Name'][0:5])

# Another way to get the 'Name' column from the XLSX file
print("\nNames from XLSX file:\n", df_xlsx['Name'])

# Get multiple columns from the TXT file
print("\nSelected columns from TXT file:\n", df_txt[['Name', 'Type 1', 'HP']])
