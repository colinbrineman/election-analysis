# Create variable for title
title = "Colorado Congressional Election Results"

# Import dependencies
import csv
import os

# Create variable for election data input
file_to_load = os.path.join("resources", "election_results.csv")

# Create variable for election analysis output
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total votes at 0
total_votes = 0

# Create candidate list
candidate_list = []

# Create candidate vote counts dictionary
candidate_count = {}

# Create county list
county_list = []

# Create county vote counts dictionary
county_count = {}

# Create variable for winning candidate
winning_candidate = ""

# Initialize winning candidate votes at 0
winning_votes = 0

# Initialize winning candidate percentage at 0
winning_percentage = 0

# Create variable for largest county
largest_county = ""

# Initialize largest county votes at 0
largest_votes = 0

# Initialize largest county percentage at 0
largest_percentage = 0

# Read csv for election data input
with open(file_to_load) as election_data:

    # Convert csv to list of dictionaries
    reader = csv.reader(election_data)

    # Read csv header
    header = next(reader)

    # Iterate over csv rows
    for row in reader:

        # Add to total votes
        total_votes = total_votes + 1

        # Get candidate name from each row
        candidate_name = row[2]

        # Get county name from each row
        county_name = row[1]

        # Create if statement to get unique candidate names
        if candidate_name not in candidate_list:

            # Add unique candidate names to candidate list
            candidate_list.append(candidate_name)

            # Begin tracking candidate vote counts
            candidate_count[candidate_name] = 0

        # Add to candidate vote counts
        candidate_count[candidate_name] += 1

        # Create if statement to get unique county names
        if county_name not in county_list:

            # Add unique county names to county list
            county_list.append(county_name)

            # Begin tracking the county vote counts
            county_count[county_name] = 0

        # Add to county vote counts
        county_count[county_name] += 1
        
# Write to txt for election analysis output
with open(file_to_save, "w") as election_analysis:

    # Create f-string for title header
    title_header = (
        f"\n***************************************\n"
        f"{title}\n"
        f"***************************************\n")

    # Print f-string for title header
    print(title_header, end="")

    # Write f-string for title header to txt
    election_analysis.write(title_header)
    
    # Create f-string for total results header
    total_results_header = (
        f"\n---------------------------------------\n"
        f"Total Results\n"
        f"---------------------------------------\n")

    # Print f-string for total results header    
    print(total_results_header, end="")

    # Write f-string for total results header to txt
    election_analysis.write(total_results_header)   
    
    # Create f-string for total results
    total_results = (
        f"Total Votes: {total_votes:,}\n")

    # Print f-string for total results    
    print(total_results, end="")

    # Write f-string for total results to txt    
    election_analysis.write(total_results)

    # Create f-string for county results header    
    county_results_header = (
        f"\n---------------------------------------\n"
        f"County Results\n"
        f"---------------------------------------\n")

    # Print f-string for county results header
    print(county_results_header, end="")

    # Write f-string for county results to txt        
    election_analysis.write(county_results_header)

    # Iterate over county vote counts dictionary
    for county_name in county_count:
        
        # Get county vote counts
        county_votes = county_count.get(county_name)
        
        # Calculate county percentages
        county_percentage = float(county_votes) / float(total_votes) * 100

        # Create f-string for county results
        county_results = (
            f"{county_name}: {county_percentage:.1f}% ({county_votes:,})\n")
        
        # Print f-string for county results
        print(county_results, end="")
        
        # Write f-string for county results to txt
        election_analysis.write(county_results)
        
        # Create if statement to identify largest county
        if (county_votes > largest_votes) and (county_percentage > largest_percentage):
            
            # Identify county vote count
            largest_votes = county_votes
            
            # Identify county percentage
            largest_percentage = county_percentage
            
            # Identify name
            largest_county = county_name

    # Create f-string for largest county header
    largest_results_header = (
        f"\n---------------------------------------\n"
        f"Largest County Results\n"
        f"---------------------------------------\n")

    # Print f-string for largest county header
    print(largest_results_header, end="")

    # Write f-string for largest county header to txt
    election_analysis.write(largest_results_header)    

    # Create f-string for largest county results
    largest_results = (
        f"Largest County: {largest_county}\n"
        f"Largest County Votes: {largest_votes:,}\n"
        f"Largest County Percentage: {largest_percentage:.1f}%\n")
    
    # Print f-string for largest county results
    print(largest_results, end="")

    # Write f-string for largest county results to txt
    election_analysis.write(largest_results)

    # Create f-string for candidate results header
    candidate_results_header = (
        f"\n---------------------------------------\n"
        f"Candidate Results\n"
        f"---------------------------------------\n")
 
    # Print f-string for candidate results header
    print(candidate_results_header, end="")

    # Write f-string for candidate results header to txt
    election_analysis.write(candidate_results_header)
        
    # Iterate over candidate vote counts dictionary
    for candidate_name in candidate_count:

        # Get candidate vote counts
        candidate_votes = candidate_count.get(candidate_name)
        
        # Calculate candidate percentages
        candidate_percentage = float(candidate_votes) / float(total_votes) * 100
        
        # Create f-string for candidate results
        candidate_results = (
            f"{candidate_name}: {candidate_percentage:.1f}% ({candidate_votes:,})\n")

        # Print f-string for candidate results
        print(candidate_results, end="")
        
        # Write f-string for candidate results to txt
        election_analysis.write(candidate_results)

        # Create if statement to identify winning candidate
        if (candidate_votes > winning_votes) and (candidate_percentage > winning_percentage):
            
            # Identify candidate vote count
            winning_votes = candidate_votes
            
            # Identify candidate vote percentage
            winning_percentage = candidate_percentage
            
            # Identify candidate name
            winning_candidate = candidate_name

    # Create f-string for winning candidate results header
    winner_results_header = (
        f"\n---------------------------------------\n"
        f"Winning Candidate Results\n"
        f"---------------------------------------\n")
    
    # Print f-string for winning candidate results header
    print(winner_results_header, end="")

    # Write f-string for winning candidate results header to txt
    election_analysis.write(winner_results_header)

    # Create f-string for winning candidate
    winner_results = (
        f"Winning Candidate: {winning_candidate}\n"
        f"Winning Candidate Votes: {winning_votes:,}\n"
        f"Winning Candidate Percentage: {winning_percentage:.1f}%\n")
    
    # Print f-string for winning candidate
    print(winner_results, end="")

    # Write f-string for winning candidate to txt
    election_analysis.write(winner_results)