# Module 3 challenge - PyPoll
# https://courses.bootcampspot.com/courses/2974/assignments/45813?module_item_id=845393

import os
import csv

csv_path = os.path.join('../PyPoll', 'Resources', 'election_data.csv')

# read CSV file
with open(csv_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # read and print the header row
    csv_header = next(csvreader)

    # read each row of data after the header
    # count total number of votes
    # list of candidates who received votes
    vote_count = []
    candidates = []
    candidate_vote_count = []
    candidate_total_votes = []
    candidate_percentage_votes = []

    for row in csvreader:
        total_votes = vote_count.append(row[0])
        candidate_vote_count.append(row[2])
        if row[2] not in candidates:
            candidates.append(row[2])

    print(len(vote_count))

    # total number of votes each candidate won
    # percentage of votes each candidate won
    for i in range(len(candidates)):
        candidate_count = candidate_vote_count.count(candidates[i])
        candidate_total_votes.append(candidate_count)
        percentage_votes = (candidate_count / (len(vote_count))) * 100
        candidate_percentage_votes.append(round(percentage_votes, 2))

    # winner candidate
    winner = max(candidate_total_votes)
    winner_index = candidate_total_votes.index(winner)
    winning_candidate = candidates[winner_index]

    # print results to the terminal
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str((len(vote_count))))
    print("-------------------------")
    print(f"{candidates[0]}: {candidate_percentage_votes[0]}% ({str(candidate_total_votes[0])})")
    print(f"{candidates[1]}: {candidate_percentage_votes[1]}% ({str(candidate_total_votes[1])})")
    print(f"{candidates[2]}: {candidate_percentage_votes[2]}% ({str(candidate_total_votes[2])})")
    print("-------------------------")
    print("Winner: " + winning_candidate)

# export a text file with the results in new line each
with open('../PyPoll/analysis/Results.txt', "w") as output:
    output.write(
        '\n'.join([
            "Election Results",
            "-------------------------",
            "Total Votes: "+ str((len(vote_count))),
            "-------------------------",
            f"{candidates[0]}: {candidate_percentage_votes[0]}% ({str(candidate_total_votes[0])})",
            f"{candidates[1]}: {candidate_percentage_votes[1]}% ({str(candidate_total_votes[1])})",
            f"{candidates[2]}: {candidate_percentage_votes[2]}% ({str(candidate_total_votes[2])})",
            "-------------------------",
            "Winner:  "+ winning_candidate
        ]))
