#import module for creating paths in operating system
import os

#import module for reading csv's
import csv

#set relative path to find budget data. Starting directory is the PyBank folder.
budgetPath = os.path.join("resources", "budget_data.csv")

#read budget csv
with open(budgetPath) as budgetCsv:
    budgetRead = csv.reader(budgetCsv, delimiter=",")

    #read header row
    header = next(budgetRead)

    #create dictionary for profits/losses data
    dictionary = {rows[0]:int(rows[1]) for rows in budgetRead}
    profits = list(dictionary.values())
    dates = list(dictionary.keys())

    #initiate variables needed for loops
    total = sum(profits)
    count = len(dictionary)
    change = 0
    lsChange = []

    #loop to create list of changes in profits/losses
    for x in range(1,count):
        change = profits[x] - profits[x-1]
        lsChange.append(change)

    #calculate max profit, max loss, and avg profit/loss and assign to variables
    avgChange = sum(lsChange)/len(lsChange)
    maxinc = max(lsChange)
    maxdec = min(lsChange)
    maxdate = dates[(lsChange.index(maxinc))+1]
    mindate = dates[(lsChange.index(maxdec))+1]
    
    #test to see if all values correct
    print(count,total,avgChange,maxdec,maxinc)
    print(maxdate)
    print(mindate)