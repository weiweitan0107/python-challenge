# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.','Resources', 'budget_data.csv')

print(csvpath)

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print(csv_header)
    print(csvreader)
    
    Totalmonth = 0
    TotalPnL =0 
    LastPnL = 0
    CurrentPnLchange = 0
    TotalPnLchange = 0
    MaxIncPnLchange = 0
    MaxIncPnLchangeDate = 0
    MaxDecPnLchange = 0
    MaxDecPnLchangeDate = 0

    # Read each row of data after the header
    for row in csvreader:
        Totalmonth += 1   # count total months
        TotalPnL += int(row[1])   #count total profit-n-loss
        
        if Totalmonth > 1:  #ignore the 1st month, since it has no previous month to calculate
            CurrentPnLchange = int(row[1]) - LastPnL # change in profit-n-loss between this month and previous month
            
            TotalPnLchange += CurrentPnLchange
            
            if CurrentPnLchange > MaxIncPnLchange:  #compare and record the max increase in profits (date and amount) 
                MaxIncPnLchange = CurrentPnLchange
                MaxIncPnLchangeDate = row[0]

            if CurrentPnLchange < MaxDecPnLchange:  #compare and record the minimal increase in profits (date and amount) 
                MaxDecPnLchange = CurrentPnLchange
                MaxDecPnLchangeDate = row[0]

        LastPnL = int(row[1])  # save this month's profit-n-loss
    

    print(Totalmonth)
    print(TotalPnL)
    print(TotalPnLchange/(Totalmonth-1))  

    # print the Results
    print("Financial Analysis")
    print("....................................................................................")
    print("total months: " + str(Totalmonth))
    print("Total: " + "$" + str(TotalPnL))
    print("Average change: " + "$" + str(TotalPnLchange/(Totalmonth-1)))  # average monthly change, the 1st month was ingored, so N-1
    print("Greatest Increase in Profits: " + str(MaxIncPnLchangeDate) + " " + "($" + str(MaxIncPnLchange) + ")")
    print("Greatest Decrease in Profits: " + str(MaxDecPnLchangeDate) + " " + "($" + str(MaxDecPnLchange) + ")")

    # output to a text file
    file = open("output.txt","w")
    file.write("Financial Analysis" + "\n")
    file.write("...................................................................................." + "\n")
    file.write("total months: " + str(Totalmonth) + "\n")
    file.write("Total: " + "$" + str(TotalPnL) + "\n")
    file.write("Average change: " + "$" + str(TotalPnLchange/(Totalmonth-1)) + "\n")
    file.write("Greatest Increase in Profits: " + str(MaxIncPnLchangeDate) + " " + "($" + str(MaxIncPnLchange) + ")" + "\n")
    file.write("Greatest Decrease in Profits: " + str(MaxDecPnLchangeDate) + " " + "($" + str(MaxDecPnLchange) + ")" + "\n")
    file.close()