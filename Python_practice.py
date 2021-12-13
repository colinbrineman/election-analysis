counties = ["Arapahoe","Denver","Jefferson"]

print("~ for loop iterating over counties ~")
for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

print("~ for loop iterating over counties_dict ~")
for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438}]

print("~ for loop iterating over voting_data ~")
for county_dict in voting_data:
    print(county_dict)

print("~ for loop iterating over voting_data to print counties ~")
for i in range(len(voting_data)):
      print(voting_data[i]['county'])
for county_dict in voting_data:
     print(county_dict['county'])

print("~ for loop iterating over voting_data to print counties & values ~")
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

print("~ f-string example ~")
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

print("~multiline f-string example~")
candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes} number of votes."
    f"The total number of votes in the election was {total_votes}."
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)