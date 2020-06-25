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

#Print Header
print("Financial Analysis")
print("------------------")

#Counts the total amount of months
month = budget_file_df["Date"].count()
print("Total Months: " + str(month) + "")

#Totals up the amount of profit/losses
total = budget_file_df["Profit/Losses"].sum()
print("Total: $" + str(total) + "")

#Finds the Average Change between periods
difference = budget_file_df["Profit/Losses"].diff()
average = round(difference.mean(), 2)
print("Average Change: $" + str(average) + "")

#Calculates the Greatest Increase in Profits
max_inc = budget_file_df[["Date", "Profit/Losses"]].max()
max_increase = round(difference.max(), 2)
#max_month = [budget_file_df['Profit/Losses'] > '100000']
print("Greatest Increase in Profits: " + " $" + str(max_increase) + "")

#Calculates the Greatest Decrease in Profits
max_dec = budget_file_df["Profit/Losses"].min()
max_decrease = round(difference.min(), 2)
print("Greatest Decrease in Profits: $" + str(max_decrease) + "")

#Part 2

# Set variable for output file
output_file = os.path.join(".", "analysis","budget.csv")

#  Opens and writes the file budget.csv
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-------------------"])

    # Write in rows
    writer.writerow(["Total Months: " + str(month) + ""])
    writer.writerow(["Total: $" + str(total) + ""])
    writer.writerow(["Average Change: $" + str(average) + ""])
    writer.writerow(["Greatest Increase in Profits: " + " $" + str(max_increase) + ""])
    writer.writerow(["Greatest Decrease in Profits: $" + str(max_decrease) + ""])
    
    