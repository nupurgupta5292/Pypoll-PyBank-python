# Importing essential modules
import os
import csv
import statistics
import subprocess, sys

# Empty list for storing names of counties
county_name = []
# Empty list for storing names of candidates
candidates_name = []
# Empty list for storing Voter IDs
voter_ids = []
# Empty list for storing vote counts for each candidate
candidate_count = []
candidate_percentage = []

# Setting up path for file
csvpath = os.path.join("C:/Users/nites/Desktop/UT-TOR-DATA-PT-01-2020-U-C/03-Python/Instructions/PyPoll/Resources","election_data.csv")

# Opening the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # To skip header
    next(csvreader)

    # For loop for reading all rows in the CSV and adding them to specific lists
    for row in csvreader:
        voter_ids.append(row[0])
        county_name.append(row[1])
        candidates_name.append(row[2])
    
    # To print headers and total number of votes casted by calculating the length of list of voters
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {str(len(voter_ids))}")
    print(f"-------------------------")

    # Applying set function to create a unique list of candidate names
    candidates_name_unique_set = set(candidates_name)
    # print(candidates_name_unique_set)

    #Transferring unique names from set to another list to enable its use in loops
    candidates_name_unique = list(candidates_name_unique_set)
    # print(candidates_name_unique)

    # Counting votes received by each candidate and storing it in a separate list
    candidate_count = [ candidates_name.count(candidates_name_unique[i]) for i in range(0,len(candidates_name_unique)) ]
    # print(candidate_count)

    # Counting votes received by each candidate and storing it in a separate list
    candidate_percentage = [((candidate_count[i]/len(voter_ids) * 100)) for i in range(0,len(candidate_count)) ]
    # print(candidate_percentage)

    #Printing Vote count and percentage for each candidate using three different lists or candidate name, vote count and percentage
    for i in range(0,len(candidate_count)):
        print(f"{candidates_name_unique[i]}: {str(round(candidate_percentage[i],3))}% ({str(candidate_count[i])})") 

    print(f"-------------------------")

    #Printing the name of the winner of the elections, present on index corressponding to the highest percentage of votes received
    print(f"Winner: {candidates_name_unique[candidate_percentage.index(max(candidate_percentage))]}")

#output = subprocess.check_output([sys.executable, "C:/Users/nites/Desktop/python-challenge/PyPoll/Main.py"])
#with open('PyPoll_output.txt', 'wb') as outfile:
    #outfile.write(output)

#outfile.close()




