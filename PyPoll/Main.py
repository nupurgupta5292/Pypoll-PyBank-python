# Importing essential modules
import os
import csv

# Empty lists for storing names of counties, name of candidates and vote counts for each candidate from csv
county_name = []
candidates_name = []
voter_ids = []

# Empty lists for storing vote counts and percentages for each candidate
candidate_count = []
candidate_percentage = []

# Empty lists for storing sorted lists of names, vote counts and percentages for each candidate
candidate_count_sorted = []
candidate_percentage_sorted = []
candidates_name_unique_sorted = []

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

    #Creating a list of unique names from set to enable its use in loops
    candidates_name_unique = list(candidates_name_unique_set)
    # print(candidates_name_unique)

    # Counting votes received by each candidate and storing it in a separate list
    candidate_count = [ candidates_name.count(candidates_name_unique[i]) for i in range(len(candidates_name_unique)) ]
    # print(candidate_count)

    # Calculating votes percentage for each candidate and storing it in a separate list
    candidate_percentage = [((candidate_count[i]/len(voter_ids) * 100)) for i in range(len(candidate_count)) ]
    # print(candidate_percentage)

    #Sorting vote count and percentage lists in descending order
    candidate_count_sorted = sorted(candidate_count,key=None,reverse=True)
    candidate_percentage_sorted = sorted(candidate_percentage,key=None,reverse=True)
    # print(candidate_count_sorted)
    # print(candidate_percentage_sorted)

    #Sorting Candidate name list according to newly sorted candidate count lists so that correct vote count is corresponding to each candidate
    candidates_name_unique_sorted = [(candidates_name_unique[candidate_count.index(candidate_count_sorted[i])]) for i in range(len(candidate_count))]
    #print(candidates_name_unique_sorted)

    #Printing Vote count and percentage for each candidate using the three lists for candidate name, vote count and percentage
    for i in range(0,len(candidate_count)):
        print(f"{candidates_name_unique_sorted[i]}: {str(round(candidate_percentage_sorted[i],3))}% ({str(candidate_count_sorted[i])})") 
    
    print(f"-------------------------")

    #Printing the name of the winner of the elections, present on index corressponding to the highest percentage of votes received
    print(f"Winner: {candidates_name_unique[candidate_percentage.index(max(candidate_percentage))]}\n")

# Exporting the output to a text file
output_file = open('C:/Users/nites/Desktop/python-challenge/PyPoll/PyPoll_output.txt', 'w')
output_file.write("Election Results\n")
output_file.write("-------------------------\n")
output_file.write("Total Votes: " + str(len(voter_ids)) + "\n")
output_file.write("-------------------------\n")
for i in range(0,len(candidate_count)):
    output_file.write(candidates_name_unique_sorted[i] + ": " + str(round(candidate_percentage_sorted[i],3)) + "% " + "(" + str(candidate_count_sorted[i]) + ")\n")
output_file.write("-------------------------\n")
output_file.write("Winner: " + candidates_name_unique[candidate_percentage.index(max(candidate_percentage))] + "\n")
output_file.close()




