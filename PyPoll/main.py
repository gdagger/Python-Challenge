import csv

path = "/Users/glena.dagger/Desktop/BootCamp/AssignmentRepositories/Python-Challenge/PyPoll/"

with open(path + "Resources/election_data.csv", 'r') as f:
    reader = csv.reader(f)

    
    header = next(reader)
#    print(header)


    total_votes = 0
    candidate_list = []
    vote_list = []
    

    for row in reader:
        total_votes += 1

        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            vote_list.append(0)

        for i in range(len(candidate_list)):
            if candidate_list[i] == row[2]:
                vote_list[i] += 1

    election_list = list(zip(candidate_list,vote_list))
