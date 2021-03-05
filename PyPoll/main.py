# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes=[]
khan_votes=[]
correy_votes=[]
li_votes=[]
otooley_votes=[]

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    for row in (csvreader):
    #puts voter ID in a list so I can use the len funtion to figure out count of votes
        total_votes.append(row[0])

        if row[2]=="Khan":
          khan_votes.append(row[0])
        elif row[2] == "Correy":
          correy_votes.append(row[0])
        elif row[2]=="Li":
           li_votes.append(row[0])
        elif row[2]=="O'Tooley":
            otooley_votes.append(row[0])

percent_value_khan = len(khan_votes)/len(total_votes)*100
percent_value_correy = len(correy_votes)/len(total_votes)*100
percent_value_li = len(li_votes)/len(total_votes)*100
percent_value_otooley = len(otooley_votes)/len(total_votes)*100

#creating dictionary so I can tie candidates together and find maximum number of votes to declare winner
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
count_votes = [len(khan_votes), len(correy_votes), len(li_votes), len(otooley_votes)]

#zip into tuples
candidates_votes = {zip(candidates,count_votes)}

winner = max(count_votes) 

print("Election Results")
print("----------------------------------------------------------------")
print(f"Total Votes: {len(total_votes)}")
print("----------------------------------------------------------------")
print(f"Khan: {round(percent_value_khan,2)}% ({len(khan_votes)})")
print(f"Correy: {round(percent_value_correy,2)}% ({len(correy_votes)})")
print(f"Li: {round(percent_value_li,2)}% ({len(li_votes)})")
print(f"O'Tooley: {round(percent_value_otooley,2)}% ({len(otooley_votes)})")
print("----------------------------------------------------------------")
print(f"Winner: {winner}") #could not figure out how to get Khan 
print("----------------------------------------------------------------")

# Specify the file to write to
output_path = os.path.join("Analysis", "voter_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as file:

        # Write the first row (column headers)
    file.write("Election Results\n")
    file.write("----------------------------------------------------------------\n")
    file.write(f"Total Votes: {len(total_votes)}\n")
    file.write("----------------------------------------------------------------\n")
    file.write(f"Khan: {round(percent_value_khan,2)}% ({len(khan_votes)})\n")
    file.write(f"Correy: {round(percent_value_correy,2)}% ({len(correy_votes)})\n")
    file.write(f"Li: {round(percent_value_li,2)}% ({len(li_votes)})\n")
    file.write(f"O'Tooley: {round(percent_value_otooley,2)}% ({len(otooley_votes)})\n")
    file.write("----------------------------------------------------------------\n")
    file.write(f"Winner: {winner}\n") #could not figure out how to get Khan 
    file.write("----------------------------------------------------------------\n")
