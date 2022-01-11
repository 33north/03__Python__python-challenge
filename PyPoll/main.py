# Importing modules/packagesimport csvimport os# Define the csvpath variable using os.path.join methodcsvpath = os.path.join("resources", "election_data.csv")# Empty lists and variablestotal_votes = 0winner = ""each_candidate_data = []# Function that does the following:#   - Generate unique list of candidates#   - Get a list of total vote count per candidate#   - Get a list of calculated percentate of vote per candidate#   - Returns a dictionary that the key-values are listdef candidates_and_votes(voter_list, num_votes):    candidate_list = []    candidate_only_list = []    candidate_vote_count = []    candidate_vote_percent = []        for i in range(0, len(voter_list)):        if not voter_list[i][2] in candidate_list:            candidate_list.append(voter_list[i][2])        candidate_only_list.append(voter_list[i][2])    for i in range(0, len(candidate_list)):           candidate_vote_count.append(candidate_only_list.count(candidate_list[i]))        percent_vote = (candidate_vote_count[i]/num_votes) * 100        candidate_vote_percent.append(percent_vote)        candidate_vote_dict = {"unique candidate list": candidate_list,                           "total vote of each candidate": candidate_vote_count,                           "percent of each candidate": candidate_vote_percent}            return candidate_vote_dict# def candidate_output(candidate_dict):#     prompt_list = # Use context manager to open and read the election_data.csv filewith open(csvpath, "r") as election_data:    # Reads the data from the election_data.csv via the csv.reader method into csv_reader variable    csv_reader = csv.reader(election_data, delimiter = ",")    csv_header = next(csv_reader)        # List comprehension reads each row of csv_reader object and appends to election_data_list list    election_data_list = [voter for voter in csv_reader]        # Finds total months based on length of election_data_list list    total_votes = len(election_data_list)        each_candidate_data = candidates_and_votes(election_data_list, total_votes)    print("""Election Results\n----------------------------""")    print(f"Total Votes: {total_votes}")    print("----------------------------")    # for i in range()    # print(f"{each_candidate_data[]}: {each_candidate_votes[1][0]:.3f}% ({each_candidate_votes[0][0]})")    # print(f"{unique_candidate_list[1]}: {each_candidate_votes[1][1]:.3f}% ({each_candidate_votes[0][1]})")    # print(f"{unique_candidate_list[2]}: {each_candidate_votes[1][2]:.3f}% ({each_candidate_votes[0][2]})")    # print(f"{unique_candidate_list[3]}: {each_candidate_votes[1][3]:.3f}% ({each_candidate_votes[0][3]})")    # print("----------------------------")    # print(f"Winner: ")    # print("----------------------------")        print(each_candidate_data[list(each_candidate_data.keys())[0]])    print(each_candidate_data[list(each_candidate_data.keys())[1]])    print(each_candidate_data[list(each_candidate_data.keys())[2]])