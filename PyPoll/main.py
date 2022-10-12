##  MODULE 3 HOMEWORK
##  PyPoll
##  Glen Dagger

# Import csv module to read contents of file
import csv

# Import path from os module to designate file path
from os import path


## VARIABLES

# Set total vote counter to 0
total_votes = 0

# Create empty candidate list
candidates = []

# Create empty vote count list
candidate_votes = []


## READ DATA FROM CSV FILE

# Store csv file path for 'election_data.csv' in csvpath variable
csvpath = path.join('..','PyPoll','Resources','election_data.csv')

# Open election_data.csv file to read data
with open(csvpath,'r') as file:

    # Create reader object to read election_data.csv
    csvreader = csv.reader(file)

    # Store header using next() function so For loop begins with first row of data
    header = next(csvreader)

    # Iterate through each row of election_data.csv to collect relevant data
    for row in csvreader:

        # Increment total vote counter by 1 for each row
        total_votes += 1

        # Check if candidate name is not already in the list of candidates
        if row[2] not in candidates:

            # If not, append it to the list
            candidates.append(row[2])

            # Append an element of 0 for each new candidate
            candidate_votes.append(0)
        
        ## FOR LOOP
        # For loop to count number of votes for each individual candidate
        for i in range(len(candidates)):

            # Check which candidate matches the candidate name in each row
            if candidates[i] == row[2]:

                # Increment the corresponding vote count for that candidate in candidate_votes
                candidate_votes[i] += 1

        ## END FOR LOOP


## DATA ANALYSIS

# List comprehension to calculate and store voting percentage for each candidate in vote_percent list
vote_percent = [round((vote/total_votes*100),2) for vote in candidate_votes]

# Set winning vote counter = 0
winning_votes = 0

# For loop to run same number of times as number of candidates
for i in range(len(candidates)):

    # Check if each vote amount is greater than current max vote count
    if candidate_votes[i] > winning_votes:

        # If so, update current max vote count
        winning_votes = candidate_votes[i]

        # Update current winning candidate
        winning_candidate = candidates[i]


## ELECTION RESULTS

# Create a list of strings for election results
election_results = ["\nElection Results",
                    "-------------------------",
                    f"Total Votes: {total_votes}",
                    "-------------------------",
                    f"{candidates[0]}: {vote_percent[0]}% ({candidate_votes[0]})",
                    f"{candidates[1]}: {vote_percent[1]}% ({candidate_votes[1]})",
                    f"{candidates[2]}: {vote_percent[2]}% ({candidate_votes[2]})",
                    "-------------------------",
                    f"Winner: {winning_candidate}",
                    "-------------------------\n"]

## PRINT IN TERMINAL
# Print election results
print('\n\n'.join(election_results))


## WRITE TO OUTGOING TEXT FILE
# Store file path for new outgoing file
outpath = path.join('..','PyPoll','Analysis','election_summary.txt')

# Open new outgoing text file to write results
with open(outpath,'w') as outfile:

    # Write results to outgoing text file
    outfile.write('\n\n'.join(election_results))