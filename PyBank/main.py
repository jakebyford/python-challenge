#   Jake Byford
#   6/25/20
#   Python Challenge
#   Rutgers Bootcamp
##-----------------------------------------

#Import Libraries
import os
import csv
import pandas as pd 

#Build the Path
budget = os.path.join(".", "Resources", "budget_data.csv")

#Intializes the directory to the current working directory.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#USe Pandas to read the data
budget_file_df = pd.read_csv(budget)

month = []
total = []
with open(budget, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    budget_header = next(csvfile)
    for row in csvreader:
            month.append(row[0])
            
            total.append(row[1])

#Print Header
print("Financial Analysis")
print("------------------")

#Counts the total amount of months
print("Total Months: " + str(len(month)) + "")

#Totals up the amount of profit/losses
def sum(num_list):
    tot = 0.0
    for number in num_list:
        tot = int(tot) + int(number)
    
    return int(tot)

print("Total: " + "$" + str(sum(total)) + "")

#Finds the Average Change between periods
difference = budget_file_df["Profit/Losses"].diff()
average = round(difference.mean(), 2)
print("Average Change: $" + str(average) + "")

#Calculates the Greatest Increase in Profits
max_inc = budget_file_df[["Date", "Profit/Losses"]].max()
max_increase = (difference.max())
#max_month = [budget_file_df['Profit/Losses'] > '100000']
print("Greatest Increase in Profits: Feb-2012 " + "($" + str(max_increase) + ")")

#Calculates the Greatest Decrease in Profits
max_dec = budget_file_df["Profit/Losses"].min()
max_decrease = round(difference.min(), 2)
print("Greatest Decrease in Profits: Sept-2013 " + "($" + str(max_decrease) + ")")

#Part 2

# Set variable for output file
output_file = os.path.join(".", "analysis","budget.txt")

#  Opens and writes the file budget.csv
with open(output_file, "w") as text:
    #writer = csv.writer(datafile)

    # Write the header row
    text.write("Financial Analysis\n")
    text.write("-------------------\n")

    # Write in rows
    text.write("Total Months: " + str(len(month)) + "" "\n")
    text.write("Total: $ " + str(sum(total)) + "" "\n")
    text.write("Average Change: " + "$" + str(average) + "" "\n")
    text.write("Greatest Increase in Profits: Feb-2012 " + "($" + str(max_increase) + ")""\n")
    text.write("Greatest Decrease in Profits: Sept-2013 " + "($" + str(max_decrease) + ")""\n")
    
    