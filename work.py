import os
import csv

# define the directory where the csv files are stored
csv_directory = 'C:/Users/vibi/Documents/clg/Data Science/project covid/py/csv'

# create a list to hold the file names
csv_files = []

# iterate through the files in the directory and add csv files to the list
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        csv_files.append(filename)

# create a new csv file to write the results to
with open("Output.csv", mode="w") as output_file:
    output_writer = csv.writer(output_file)

    # iterate through each csv file
    for filename in csv_files:
        # remove the .csv extension from the file name
        name_without_extension = os.path.splitext(filename)[0]

        with open(csv_directory + filename, mode="r") as input_file:
            input_reader = csv.reader(input_file)

            # get the column titles from the first row of the CSV file
            column_titles = next(input_reader)

            # find the row containing "India" and copy its contents to a list
            india_row = []
            for row in input_reader:
                if "India" in row:
                    india_row = row

            # write the filename, column titles, and india row data to the output file
            output_writer.writerow([name_without_extension] + column_titles + india_row)
