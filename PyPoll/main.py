# Import dependencies and create file path to csv file.
import os
import csv
poll_csvpath = os.path.join("Resources", "election_data.csv")

# Open csv as reader, read through rows and run for loops to capture voter ids, candidates, and candidate votes in lists.
with open(poll_csvpath) as poll_csvfile:
    poll_csvreader = csv.reader(poll_csvfile, delimiter=",")
    poll_csvreader_header = next(poll_csvreader)
    voter_id_list = []
    candidate_list = []
    votercounter = []
    percentlist = []
    for row in poll_csvreader:
        voter_id_list.append(row[0])
        total_votes = (len(voter_id_list))
        candidate_option = row[2]
        if candidate_option not in candidate_list:
            candidate_list.append(candidate_option)
            votercounter.append(1)
        else: 
            i = 0
            for candidate in candidate_list:
                if candidate_list[i] == candidate_option:
                    votercounter[i] += 1
                    break
                i += 1 
# Run for loop through voter counter list to determine percentage of votes won by each candidate and the winner.
    winnervotes = 0 
    v = 0
    for votes in votercounter:
        voterpercent = votes/total_votes*100
        percentlist.append(voterpercent)
        if votercounter[v] > winnervotes:
            winnervotes = votercounter[v]
            winningint = v
            pollwinner = candidate_list[v]  
        v += 1

# Create output file, print results to terminal, and write results to output file.
output_file = os.path.join("Analysis", "election_results.txt")
with open(output_file,"w", newline="") as datafile: 
    writer = csv.writer(datafile)
    print("Election Results")
    writer.writerow(["Election Results"])
    print("-----------------------------")
    writer.writerow(["-----------------------------"])
    print(f"Total Votes: {total_votes}")
    writer.writerow([f"Total Votes: {total_votes}"])
    print("-----------------------------")
    writer.writerow(["-----------------------------"])
    r = 0
    for results in candidate_list:
        print(f"{candidate_list[r]}: {round(percentlist[r],3)}% ({votercounter[r]})")
        writer.writerow([f"{candidate_list[r]}: {round(percentlist[r],3)}% ({votercounter[r]})"])
        r += 1
    print("-----------------------------")
    writer.writerow(["-----------------------------"])
    print(f"Winner: {pollwinner}")
    writer.writerow([f"Winner: {pollwinner}"])
    print("-----------------------------")
    writer.writerow(["-----------------------------"])       
