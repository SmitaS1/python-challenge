### First we'll import the os module
### This will allow us to create file paths across operating systems
import os

### Module for reading CSV files
import csv

csvpath = os.path.join('PyPoll','Resources','election_data.csv')

number_of_votes = 0
count_vote = 0

candidate_dic = {}

with open(csvpath) as csvfile:

    ### CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    ### Read the header row first
    csv_header = next(csvreader)

    ### Read the second row in csv file
    for i in csvreader :
        number_of_votes = number_of_votes + 1
              
        if i[2] in candidate_dic :
            candidate_dic[i[2]] += 1
           
        else :
            candidate_dic[i[2]] = 1
        dic_len = str(len(candidate_dic))

    ### Calculating percentage of votes for each candidate
    vote_pct_charles= round((candidate_dic["Charles Casper Stockham"]/number_of_votes)*100, 3)
    vote_pct_Diana= round((candidate_dic["Diana DeGette"]/number_of_votes)*100, 3)
    vote_pct_Ray = round((candidate_dic["Raymon Anthony Doane"]/number_of_votes)*100, 3)
    
    ### calculating who is the winner
    if vote_pct_charles > vote_pct_Diana and vote_pct_charles > vote_pct_Ray :
        winner = "Charles Casper Stockham"
    elif vote_pct_Diana > vote_pct_charles and vote_pct_Diana > vote_pct_Ray :
        winner = "Diana DeGette"
    elif vote_pct_Ray > vote_pct_charles and vote_pct_Ray > vote_pct_Diana :
        winner = "Raymon Anthony Doane"

###Printing the result/output on terminal
print("Election Results")
print("---------------------------------")
print(f'Total Votes : {number_of_votes }') 
print("---------------------------------")   
print(f'Charles Casper Stockham : {vote_pct_charles}% ({candidate_dic["Charles Casper Stockham"]})')  
print(f'Diana DeGette : {vote_pct_Diana}% ({candidate_dic["Diana DeGette"]})')  
print(f'Raymon Anthony Doane : {vote_pct_Ray}% ({candidate_dic["Raymon Anthony Doane"]})')  
print("---------------------------------")
print(f'Winner :  {winner}')
print("---------------------------------")

### Printing the result/output in text file
### Set variable for output file
output_file = os.path.join('PyPoll','analysis','PyPolloutput.txt')

###  Open the output file
with open(output_file, "w") as outputfile:
    print("Election Results",file=outputfile)
    print("---------------------------------",file=outputfile)
    print(f"Total Votes : {number_of_votes }",file=outputfile) 
    print("---------------------------------",file=outputfile)   
    print(f'Charles Casper Stockham : {vote_pct_charles}% ({candidate_dic["Charles Casper Stockham"]})',file=outputfile)  
    print(f'Diana DeGette : {vote_pct_Diana}% ({candidate_dic["Diana DeGette"]})',file=outputfile)  
    print(f'Raymon Anthony Doane : {vote_pct_Ray}% ({candidate_dic["Raymon Anthony Doane"]})',file=outputfile)  
    print("---------------------------------",file=outputfile)
    print(f'Winner :  {winner}',file=outputfile)
    print("---------------------------------",file=outputfile)


    