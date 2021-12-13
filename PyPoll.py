# Data to retrive
    # 1. Total number of votes cast
    # 2. A complete list of candidates who received votes
    # 3. Total number of votes each candidate received
    # 4. Percentage of votes each candidate won
    # 5. The winner of the election based on popular vote

# Import dependencies
import csv
import os

# Assign variable to data file path
file_to_load = os.path.join("resources", "election_results.csv")

# Assign variable to text file path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open and assign variable to text file
with open(file_to_save, "w") as txt_file:

    # Write data to text file
    txt_file.write("Hello World")

# Open and assign variable to data file
with open(file_to_load) as election_data:

    # Assign variable to data file object
    file_reader = csv.reader(election_data)

    # Exclude header row from data file object
    headers = next(file_reader)
    print(headers)
    