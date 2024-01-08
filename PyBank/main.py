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

    #declare empty lists to read variables
    profits = []
    dates = []

    #assign csv variables to lists
    for rows in budgetRead:
        dates.append(rows[0])
        profits.append(int(rows[1]))

    #Find total profits and total months by counting the length of profit list
    total = sum(profits)
    count = len(profits)

    #initiate variables needed for loops
    change = 0
    lsChange = []

    #loop to create list of changes in profits/losses
    for x in range(1, count):                #Reference #1
        change = profits[x] - profits[x-1]   #Reference #1
        lsChange.append(change)              #Reference #1

    #calculate max profit, max loss, and avg profit/loss and assign to variables
    avgChange = round(sum(lsChange)/len(lsChange),2)
    maxinc = max(lsChange)
    maxdec = min(lsChange)

    #find the dates associated with the maximum increase and decrease in profits
    maxdate = dates[(lsChange.index(maxinc))+1]
    mindate = dates[(lsChange.index(maxdec))+1]
    
    # #test to see if all values correct
    # print(count,total,avgChange,maxdec,maxinc)
    # print(maxdate)
    # print(mindate)

    #print results to the terminal
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(count))
    print("Total: $" + str(total))
    print("Average Change: $" + str(avgChange))
    print("Greatest Increase in Profits: " + str(maxdate) + " ($" + str(maxinc) +")")
    print("Greatest Decrease in Profits: " + str(mindate) + " ($" + str(maxdec) +")")
    
#create a .txt file in the analysis folder that contains the above printout
with open("analysis/PyBankResults.txt", "w") as text:            #Reference 4
    text.write(f"""Financial Analysis
----------------------------
Total Months: {str(count)}
Total: ${str(total)}
Average Change: ${str(avgChange)}
Greatest Increase in Profits: {str(maxdate)} (${str(maxinc)})
Greatest Decrease in Profits: {str(mindate)} (${str(maxdec)})""" #Reference 4
            )
