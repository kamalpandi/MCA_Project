import os
import csv

# Define the directory where your CSV files are stored
directory = 'C:/Users/vibi/Documents/clg/Data Science/project covid/py/csv'

# Loop over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):  # Check that the file is a CSV file
        # Open the CSV file and read its contents
        with open(os.path.join(directory, filename), 'r', newline='') as input_file:
            csv_reader = csv.reader(input_file)
            header = next(csv_reader)  # Get the header row
            
            # Find the index of the Country/Region column
            country_region_index = None
            for i, column_name in enumerate(header):
                if column_name == 'Country_Region':
                    country_region_index = i
                    break
            
            # If the Country/Region column is found, look for India rows
            if country_region_index is not None:
                for row in csv_reader:
                    if row[country_region_index] == 'India':
                        # Extract the relevant data fields and column names
                        date_column_name = header[0]
                        date_value = os.path.splitext(filename)[0]  # Use the filename as the date value
                        india_data = {}
                        for i, cell_value in enumerate(row):
                            if i != country_region_index and cell_value != '':
                                column_name = header[i]
                                india_data[column_name] = cell_value
                        
                        # Write the data to a new CSV file
                        with open('output_file.csv', 'a', newline='') as output_file:
                            csv_writer = csv.writer(output_file)
                            if output_file.tell() == 0:  # Check if the file is empty
                                csv_writer.writerow([date_column_name, *india_data.keys()])
                            csv_writer.writerow([date_value, *india_data.values()])
