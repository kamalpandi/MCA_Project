import pandas as pd

# Read the CSV file into a pandas dataframe
df = pd.read_csv('output_file.csv')

# Convert the date column to datetime format
df['FIPS'] = pd.to_datetime(df['FIPS'], format='%m-%d-%Y')

# Extract the year from the date and create a new column
df['Year'] = df['FIPS'].dt.year

# Sort the dataframe by year and relevant data
df = df.sort_values(['Year', 'FIPS'], ascending=[True, False])

# Write the sorted data to a new CSV file
df.to_csv('sorted_date.csv', index=False, date_format='%m-%d-%Y')
