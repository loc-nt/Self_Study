print("Hello World")
type(3)
type("2019")
ballots = 1.341
ballots


counties = ["Arapahoe","Denver","Jefferson"]

counties[0]
counties[-3]
len(counties)
counties[0:-2]
counties[:2]
counties[1:]

counties.append("El Paso")

counties.insert(2, "El Paso 2")

abc = counties.pop(3)
abc

counties[2] = "El Paso"
counties

dcb = counties[2]
dcb = 3
dcb

list_a = ["abc", 123, 456]
list_a

counties_tuple = ("Arapahoe","Denver","Jefferson")
counties_tuple[1]


counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict["Jefferson"]
counties_dict[("Jefferson")]

counties_dict.items()
a = counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")

a
counties_dict



voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data[0]


for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():    
    print(f"{county} county has {voters:,} registered voters.")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for i in range(len(voting_data)):
    dict_name = voting_data[i]
    print(dict_name["county"])


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)



# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

import csv
dir(datetime.datetime)


dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})
dir(str)


# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()


# Calculation in Python:
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)

