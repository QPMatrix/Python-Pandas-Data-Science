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

# Filtering data
print("\nFiltering data:")
# Get all rows where 'Type 1' is 'Fire'
fire_pokemon = df_txt.loc[df_txt['Type 1'] == 'Fire']
print("\nFire type Pokémon:\n", fire_pokemon)

# Descriptive statistics
print("\nDescriptive statistics:")
# Get summary statistics for the CSV file
print("\nSummary statistics for CSV file:\n", df_csv.describe())

# Sorting data
print("\nSorting data:")
# Sort CSV data by 'Name' in descending order
sorted_df = df_csv.sort_values('Name', ascending=False)
print("\nCSV data sorted by 'Name' in descending order:\n", sorted_df)

# Additional examples

# Adding a new column
print("\nAdding a new column:")
df_csv['Total'] = df_csv['HP'] + df_csv['Attack'] + df_csv['Defense'] + df_csv['Sp. Atk'] + df_csv['Sp. Def'] + df_csv['Speed']
print("\nCSV file with new 'Total' column:\n", df_csv.head())

# Removing columns
print("\nRemoving columns:")
df_csv = df_csv.drop(columns=['Total'])
print("\nCSV file after removing 'Total' column:\n", df_csv.head())

# Saving to a new CSV file
print("\nSaving to a new CSV file:")
df_csv.to_csv('./modified_pokemon_data.csv', index=False)
print("\nData saved to 'modified_pokemon_data.csv'")

# Grouping data
print("\nGrouping data:")
grouped_df = df_csv.groupby(['Type 1']).mean()
print("\nGrouped data by 'Type 1' with mean values:\n", grouped_df)

# Merging DataFrames
print("\nMerging DataFrames:")
merged_df = pd.merge(df_csv, df_xlsx, on='Name')
print("\nMerged DataFrame based on 'Name':\n", merged_df.head())

# Handling missing data
print("\nHandling missing data:")
# Fill missing values with 0
df_csv.fillna(0, inplace=True)
print("\nCSV file after filling missing values with 0:\n", df_csv.head())

# Advanced indexing with loc and iloc
print("\nAdvanced indexing with loc and iloc:")
print("\nUsing loc to get data from row index 2 and 'Name' column:\n", df_csv.loc[2, 'Name'])
print("\nUsing iloc to get data from row index 2 and column index 1:\n", df_csv.iloc[2, 1])
