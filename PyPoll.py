# Import dependencies
import csv
import os

# Assign variable to input data file path
file_to_load = os.path.join("resources", "election_results.csv")

# Assign variable to output text file path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Declare candidate options list
candidate_options = []

# Declare candidate votes dictionary
candidate_votes = {}

# Declare winning candidate string
winning_candidate = ""

# Initialize winning vote counter
winning_count = 0

# Initialize winning vote percentage
winning_percentage = 0

# Open and analyze data file
with open(file_to_load) as election_data:

    # Read file
    file_reader = csv.reader(election_data)

    # Read header row
    headers = next(file_reader)
    
    # Print each row
    for row in file_reader:

        # Add to total vote count
        total_votes += 1

        # Print candidate name
        candidate_name = row[2]

        # Identify unique names
        if candidate_name not in candidate_options:

            # Add name to candidate list
            candidate_options.append(candidate_name)

            # Initialize candidate vote count
            candidate_votes[candidate_name] = 0

        # Add to  candidate vote count
        candidate_votes[candidate_name] += 1

# Save results to text file
with open(file_to_save, "w") as txt_file:

    # Declare election results string
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    
    # Print election results to terminal
    print(election_results, end="")

    # Save election results to text file
    txt_file.write(election_results)

    # Iterate through candidate list
    for candidate_name in candidate_votes:

        # Retrieve candidate vote count
        votes = candidate_votes[candidate_name]

        # Calculate candidate vote percentage
        vote_percentage = float(votes) / float(total_votes) * 100

        # Declare candidate results string 
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print candidate results to terminal
        print(candidate_results)

        # Save candidate results to text file
        txt_file.write(candidate_results)

        # Identify election winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # Declare winning vote count
            winning_count = votes

            # Declare winning vote percentage
            winning_percentage = vote_percentage

            # Declare winning candidate
            winning_candidate = candidate_name

    # Declare winning candidates summary string
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    # Print winning candidates summary to terminal
    print(winning_candidate_summary)

    # Save winning candidates summary to text file
    txt_file.write(winning_candidate_summary)