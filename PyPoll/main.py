import os
import csv

input_file= os.path.join("election_data.csv")
output_file= os.path.join("election_winner.txt")

def vote_percent(i):
    percentage = round((candidate_votes[i]/total_votes)*100,5)
    return percentage
    
def winner():
    if candidate_votes[0]>candidate_votes[1] and candidate_votes[0]>candidate_votes[2] and candidate_votes[0]>candidate_votes[3]:
        return candidates[0]
    elif candidate_votes[1]>candidate_votes[0] and candidate_votes[1]>candidate_votes[2] and candidate_votes[1]>candidate_votes[3]:
        return candidates[1]
    elif candidate_votes[2]>candidate_votes[0] and candidate_votes[2]>candidate_votes[1] and candidate_votes[2]>candidate_votes[3]:
         return candidates[2]
    elif candidate_votes[3]>candidate_votes[0] and candidate_votes[3]>candidate_votes[1] and candidate_votes[3]>candidate_votes[2]:
        return candidates[3]
    else: 
        print("no winner")


total_votes= 0
candidates=["Khan", "Correy", "Li", "O'Tooley"]
candidate_votes= [0,0,0,0]



with open(input_file, "r") as election_file:
    csvreader= csv.reader(election_file)

    header= next(csvreader)

    for row in csvreader:
        
        total_votes+=1

        if row[2]=="Khan":
            candidate_votes[0]= candidate_votes[0] + 1
        elif row[2]=="Correy":
            candidate_votes[1]+= 1
        elif row[2]=="Li":
            candidate_votes[2]+= 1
        else:
            candidate_votes[3]+=1
        
           

    output= (
    f"\nElection Results\n"
    f"-------------------------------------\n"
    f"Total votes: {total_votes}\n"
    f"-------------------------------------\n"
    f"Khan: {vote_percent(0)}% ({candidate_votes[0]})\n"
    f"Correy: {vote_percent(1)}% ({candidate_votes[1]})\n"
    f"Li: {vote_percent(2)}% ({candidate_votes[2]})\n"
    f"O`Tolley: {vote_percent(3)}% ({candidate_votes[3]})\n"
    f"-------------------------------------\n"
    f"Winner: {winner()}")

    print(output)

with open(output_file, "w") as writer:
     writer.write(output)