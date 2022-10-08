## Module 3 Homework

# Import csv module to read contents of file
import csv

# Import path from os module create variable for file path
from os import path

# Create variable to store path to CSV file
csvpath = path.join('..','PyPoll','Resources','election_data.csv')

# Open election_data.csv file to read data
with open(csvpath,'r') as file:

    # Create reader object to read election_data.csv
    csvreader = csv.reader(file)

    # Store header using next() function so for loop begins with first row of data
    header = next(csvreader)

    # Set total vote counter to 0
    total_votes = 0

    # Create empty candidate list
    candidates = []

    # Create empty vote count list
    candidate_votes = []

    # Iterate through each row of election_data.csv
    for row in csvreader:

        # Increment total vote counter by 1 for each row
        total_votes += 1

        # Check if candidate name is not already in the list of candidates
        if row[2] not in candidates:

            # If not, append it to the list
            candidates.append(row[2])

            # Append an element of 0 for each new candidate
            candidate_votes.append(0)
        
        # For loop to count number of votes for each individual candidate
        for i in range(len(candidates)):

            # Check which candidate matches the candidate name in each row
            if candidates[i] == row[2]:

                # Increment the corresponding vote count for that candidate in candidate_votes
                candidate_votes[i] += 1

    # List comprehension to store voting percentage of each candidate in vote_percent list
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

    # Create a list of strings for final analysis
    election_results = ("Election Results\n"
                        "-------------------------\n"
                        f"Total Votes: {total_votes}\n"
                        "-------------------------\n"
                        f"{candidates[0]}: {vote_percent[0]}% ({candidate_votes[0]})\n"
                        f"{candidates[1]}: {vote_percent[1]}% ({candidate_votes[1]})\n"
                        f"{candidates[2]}: {vote_percent[2]}% ({candidate_votes[2]})\n"
                        "-------------------------\n"
                        f"Winner: {winning_candidate}\n"
                        "-------------------------\n")

# Print final analysis 
print(election_results)

# Create variable to store file path to new outgoing file
outpath = path.join('..','PyPoll','Analysis','election_summary.txt')

# Open new outgoing text file to write results
with open(outpath,'w') as outfile:

    # Write results to outgoing text file
    outfile.write(election_results)