import os
import csv

csv_path = os.path.join("..", "Resources", "election_data.csv")
absolute = "/Users/uknowconorhealy/Downloads/RUTJER201809DATA3-master 14/03-Python/Homework/Instructions/PyPoll/Resources/election_data.csv"

total_votes = 0
candidate_options = []
candidates = {}
candidate_votes = {}
winner=[]
most_votes = {}

with open(absolute) as election_data:
    reader = csv.DictReader(election_data)

    
    for row in reader:

        total_votes = total_votes + 1

        candidate_name = row["Candidate"]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)
           
        candidate_votes[candidate_name] = 0 

    each_vote = candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    vote_percentage = float(each_vote) / float(total_votes) * 100

    voter_output = f"{candidate_options}: {vote_percentage:.1f}% {each_vote}\n"

    most_votes = {}
    for candidate_name in candidates.keys():
        if candidate_votes[candidate_name] > most_votes:
            winner = candidate_name
            most_votes = candidate_votes[candidate_name]
   
election_results = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"Candidates: {candidate_options}\n"
    f"-------------------------\n"
    f"Winner: {voter_output}\n"
    f"-------------------------\n"
    f"Winner: {most_votes}\n"
    f"-------------------------\n")

print(election_results)


with open('election_output.csv', "w") as new_file:
    new_file.write(election_results)

