#import module for creating paths in operating system
import os

#import module for reading csv's
import csv

#set relative path to find budget data. Starting directory is the PyBank folder.
budgetPath = os.path.join("resources", "budget_data.csv")

#read budget csv
with open(budgetPath, "r") as budgetCsv:
    budgetRead = csv.reader(budgetCsv, delimiter=",")

    #read header row
    header = next(budgetRead)

    #loop through csv
    count = 0
    total = 0
    for rows in budgetRead:
        count = count + 1    #count of nonheader rows
        total = total + int(rows[1]) # sum of profits/losses