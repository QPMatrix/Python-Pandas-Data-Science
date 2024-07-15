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

# Reading each row
print("\nReading each row:")

# Print the second row from the TXT file
print("\nSecond row from TXT file:\n", df_txt.iloc[1])

# Print the second to fourth rows from the CSV file
print("\nSecond to fourth rows from CSV file:\n", df_csv.iloc[1:4])

# Print the first three rows from the XLSX file
print("\nFirst three rows from XLSX file:\n", df_xlsx.iloc[0:3])

# Reading a specific location (row, column)
print("\nReading a specific location (row, column):")

# Get data from the third row and second column in the XLSX file
print("\nValue from the third row and second column in XLSX file:\n", df_xlsx.iloc[2, 1])

# Iterating through rows with a for loop
print("\nIterating through rows with a for loop:")

# Iterate through each row in the XLSX file and print the index and row
for idx, row in df_xlsx.iterrows():
    print(idx, row)

# Iterate through each row in the XLSX file and print the index and 'Name' column value
print("\nIterating through rows and printing the 'Name' column:")
for idx, row in df_xlsx.iterrows():
    print(idx, row['Name'])
