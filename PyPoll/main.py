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
os.chdir(os.path.dirname(os.path.abspath(__file__)))
election = os.path.join(".", "Resources", "election_data.csv")

#Intializes the directory to the current working directory.

votes = []
khan = []
correy = []
li = []
otooley = []

#Use Pandas to read the data
election_file_df = pd.read_csv(election)

with open(election, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    for row in csvreader:
    #totvotes.append(row[0])
            votes.append(row[0])
            if row[2] == "Khan":
                khan.append(row[2])
            elif row[2] == "Correy":
                correy.append(row[2])
            elif row[2] == "Li":
                li.append(row[2])
            elif row[2] == "O'Tooley":
                otooley.append(row[2])

total_votes = len(votes)
total_khan = len(khan)
total_correy = len(correy)
total_li = len(li)
total_otooley = len(otooley)

khan_per = round(int(total_khan)/int(total_votes), 2)
correy_per = round(int(total_correy)/int(total_votes), 2)
li_per = round(int(total_li)/int(total_votes), 2)
otooley_per = round(int(total_otooley)/int(total_votes), 2)
     
#Print Header
print("Election Results")
print("------------------")

#Counts the total amount of months
vtes = election_file_df["Voter ID"].count()
print("Total Votes: " + str(vtes) + "")

print("-------------------")

#
print("Khan: "+"{:.2%}".format(khan_per) + " " + "(" + str(total_khan) + ")")
print("Correy: "+"{:.2%}".format(correy_per) + " " + "(" + str(total_correy) + ")")
print("Li: "+"{:.2%}".format(li_per) + " " + "(" + str(total_li) + ")")
print("O'Tooley: "+"{:.2%}".format(otooley_per) + " " + "(" + str(total_otooley) + ")")
print("-------------------")
print("Winner: Khan")
print("-------------------")

#Part 2
output_file = os.path.join(".", "analysis","election.txt")

#  Opens and writes the file budget.csv
with open(output_file, "w") as text:
    #writer = csv.writer(datafile)

    # Write the header row
    text.write("Election Results" "\n")
    text.write("-------------------" "\n")

    # Write in rows
    text.write("Total Votes: " + str(vtes) + "" "\n")
    text.write("-------------------" "\n")
    text.write("Khan: "+"{:.2%}".format(khan_per) + " " + "(" + str(total_khan) + ")" "\n")
    text.write("Correy: "+"{:.2%}".format(correy_per) + " " + "(" + str(total_correy) + ")" "\n")
    text.write("Li: "+"{:.2%}".format(li_per) + " " + "(" + str(total_li) + ")" "\n")
    text.write("O'Tooley: "+"{:.2%}".format(otooley_per) + " " + "(" + str(total_otooley) + ")" "\n")
    text.write("-------------------" "\n")
    text.write("Winner: Khan" "\n")
    text.write("-------------------" "\n")
    