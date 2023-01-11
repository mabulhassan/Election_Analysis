# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("..","Downloads", "election_results.csv")
# Assign a variable to save the file to a path.
#file_to_save = os.path.join("..","Downloads", "election_analysis.txt")

#add total votes counter
total_votes=0
candidate_options=[]
candidate_votes={}
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
     # Print each row in the CSV file.
    for row in file_reader:
       
  # 2. Add to the total vote count.
        total_votes += 1
     # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
    candidate_votes[candidate_name] += 1


# Print the candidate vote dictionary.
print(candidate_votes)