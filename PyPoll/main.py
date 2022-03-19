# Importing modules/packages
import csv
import os

# Define the csvpath variable using os.path.join method
csvpath = os.path.join("resources", "election_data.csv")
output = os.path.join("analysis", "election_results.txt")

# Empty lists and variables
total_votes = 0
winner = ""
each_candidate_data = []

# Function that does the following:
#   - Generate unique list of candidates
#   - Get a list of total vote count per candidate
#   - Get a list of calculated percentate of vote per candidate
#   - Returns a dictionary that the key-values are list
def candidates_and_votes(voter_list, num_votes):
    candidate_list = []
    candidate_only_list = []
    candidate_vote_count = []
    candidate_vote_percent = []
    
    for i in range(0, len(voter_list)):
        if not voter_list[i][2] in candidate_list:
            candidate_list.append(voter_list[i][2])
        candidate_only_list.append(voter_list[i][2])

    for i in range(0, len(candidate_list)):   
        candidate_vote_count.append(candidate_only_list.count(candidate_list[i]))
        percent_vote = (candidate_vote_count[i]/num_votes) * 100
        candidate_vote_percent.append(percent_vote)
    
    candidate_vote_dict = {"unique candidate list": candidate_list,
                           "total vote of each candidate": candidate_vote_count,
                           "percent of each candidate": candidate_vote_percent}
        
    return candidate_vote_dict

# Function prints out the election results
def election_results(vote_count, cand_vote_dict):
    # Overly complicatedd way to find the winner and also makes sure that if the number of candidate increases/decreases,
    # the code will find the winner based on the candidate_vote_count list variable from the candidates_and_votes function.
    winner = cand_vote_dict[list(cand_vote_dict.keys())[0]][cand_vote_dict[list(cand_vote_dict.keys())[1]].index(max(cand_vote_dict[list(cand_vote_dict.keys())[1]]))]

    print("""Election Results\n----------------------------""")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")

    for i in range(0, (len(cand_vote_dict[list(cand_vote_dict.keys())[0]]))):
        prompt_list = []
        for j in range(0, (len(cand_vote_dict))):
            prompt_list.append(cand_vote_dict[list(cand_vote_dict.keys())[j]][i])
        print(f"{prompt_list[0]}: {prompt_list[2]:.3f}% ({prompt_list[1]})")

    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

    # This writes the election results to a text file
    with open(output, "w") as csvfile:
        print("""Election Results\n----------------------------""", file = csvfile)
        print(f"Total Votes: {total_votes}", file = csvfile)
        print("----------------------------", file = csvfile)

        for i in range(0, (len(cand_vote_dict[list(cand_vote_dict.keys())[0]]))):
            prompt_list = []
            for j in range(0, (len(cand_vote_dict))):
                prompt_list.append(cand_vote_dict[list(cand_vote_dict.keys())[j]][i])
            print(f"{prompt_list[0]}: {prompt_list[2]:.3f}% ({prompt_list[1]})", file = csvfile)

        print("----------------------------", file = csvfile)
        print(f"Winner: {winner}", file = csvfile)
        print("----------------------------", file = csvfile)

# Use context manager to open and read the election_data.csv file
with open(csvpath, "r") as election_data:
    # Reads the data from the election_data.csv via the csv.reader method into csv_reader variable
    csv_reader = csv.reader(election_data, delimiter = ",")
    csv_header = next(csv_reader)
    
    # List comprehension reads each row of csv_reader object and appends to election_data_list list
    election_data_list = [voter for voter in csv_reader]
    
    # Finds total months based on length of election_data_list list
    total_votes = len(election_data_list)
    
    # Saves the returned results from candidates_and_votes function
    each_candidate_data = candidates_and_votes(election_data_list, total_votes)

    # Prints out election results
    election_results(total_votes, each_candidate_data)
    