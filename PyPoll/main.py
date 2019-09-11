# First we'll import the os module
# This will allow us to create file paths across operating systems

import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

print(csvpath)

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

  # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print(csv_header)
    print(csvreader)

    Total_votes = 0       # total vote casts
    Candidate_list = []   # candidate name list
    Candidate_name_and_vote = {}   # a dictionary list of "candidate_name : votes" 
    Current_candiate = ""  # candidate name of the current row
 
    for row in csvreader:
        Total_votes += 1    # calculate total vote casts

        Current_candiate = row[2]   # save the candidate name of the current row

        if Current_candiate not in Candidate_list:
            Candidate_list.append(Current_candiate)  # add the "new" candidate name to the name list
            Candidate_name_and_vote[Current_candiate] = 1  # the "new" candidate's votes start from 1
        else: 
            Candidate_name_and_vote[Current_candiate] += 1  # increase the votes of candidate by 1


#Print to screen:
print()
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(Total_votes))
print("-------------------------")

for name in Candidate_list:
    print(name + " " + "{:.3%}".format(Candidate_name_and_vote[name]/Total_votes) + " (" + str(Candidate_name_and_vote[name]) + ")") 

print("-------------------------")
print("Winner: " + max(Candidate_name_and_vote, key=Candidate_name_and_vote.get)) # The key parameter takes a function, and for each entry in the iterable, it'll find the one for which the key function returns the highest value.
print("-------------------------")

# output to a text file

file = open("output.txt","w")
file.write("Election Results " + "\n")
file.write("------------------------- " + "\n")
file.write("Total Votes: " + str(Total_votes) + "\n")
file.write("-------------------------" + "\n")

for name in Candidate_list:
    file.write(name + " " + "{:.3%}".format(Candidate_name_and_vote[name]/Total_votes) + " (" + str(Candidate_name_and_vote[name]) + ")" + "\n") 

file.write("-------------------------" + "\n")
file.write("Winner: " + max(Candidate_name_and_vote, key=Candidate_name_and_vote.get) + "\n") # The key parameter takes a function, and for each entry in the iterable, it'll find the one for which the key function returns the highest value.
file.write("-------------------------" + "\n")
    
file.close()

print("\n" + "output file generated!" + "\n")




