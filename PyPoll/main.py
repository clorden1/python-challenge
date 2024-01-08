#import necessary packages to find file path in os and read csv's
import os
import csv

#import csv using realtive path. Directory is the Pypoll folder
path = os.path.join("Resources","election_data.csv")

#read csv
with open(path) as pollcsv:
    readcsv = csv.reader(pollcsv, delimiter = ",")

    #read header row
    head = next(readcsv)

    #initaite lists for for loop
    cand = []

    #use for loop to store data in lists. Only the candidate name is needed for analysis.
    for rows in readcsv:
        cand.append(rows[2])

    #find number of votes by measure length of candidate list
    total = len(cand)
    
    #use the set() function to create a list of all unique names in the candidate list
    unique_cand = [set(cand)]               #Reference 3

    #exploratory test to display all candidates to determine variables for next loop
    #print(unique_cand)

    #declare variables to store candidate vote counts
    charles_count = 0
    diana_count = 0
    raymon_count = 0

    #for loop do find number of votes for each candidate
    for x in cand:
        if x == "Charles Casper Stockham":
            charles_count += 1              #Reference 2
        elif x == "Diana DeGette":
            diana_count += 1                #Reference 2
        else:
            raymon_count += 1               #Reference 2
    
    #Calculate the percentages of vote recieved by each candidate
    percChar = round((charles_count/total)*100,3)
    percDian = round((diana_count/total)*100,3)
    percRaym = round((raymon_count/total)*100,3)

    #Determine which candidate won the election
    if percChar > percDian and percChar > percRaym:
        winner = "Charles Casper Stockham"
    elif percDian > percChar and percDian > percRaym:
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"
    
#print results in terminal
print(                         #Reference 4
f""" Election Results                                    
 -------------------------
 Total Votes: {total}
 -------------------------
 Charles Casper Stockham: {percChar}% ({charles_count})
 Diana Degette: {percDian}% ({diana_count})
 Raymon Anthony Doane: {percRaym}% ({raymon_count})
 -------------------------
 Winner : {winner}
 -------------------------""" #Reference 4
)

#write results to a .txt file in the analysis folder
with open("analysis/PyPollResults.txt", "w") as text:
    text.write(               #Reference 4
f""" Election Results
 -------------------------
 Total Votes: {total}
 -------------------------
 Charles Casper Stockham: {percChar}% ({charles_count})
 Diana Degette: {percDian}% ({diana_count})
 Raymon Anthony Doane: {percRaym}% ({raymon_count})
 -------------------------
 Winner : {winner}
 -------------------------""" #Reference 4
)