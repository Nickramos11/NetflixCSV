import os
import csv

video = input("What show or movie are you looking for? ")

# path
csvpath = os.path.join("..", "Netflix", "netflix2020.csv")

found = False

# Opening CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop 
    for row in csvreader:
        if row[0] == video:
            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

            found = True

            # Stop at first results 
            break

    if found is False:
        print("Sorry, what you are looking for is not playing at this time!")

