# date: 10/09/2019
# developer: Humphrey Shikoli
# programming language: Python
# description: program that reads in a comma separated file and stores the data
# in a dictionary

import csv
import json

movie_dict = {}

with open("deniro.csv") as infile:
    
    csvdata = csv.reader(infile, quotechar = '"', skipinitialspace = True)
    fields = next(csvdata)
    for row in csvdata:
        print(row)
        print("\n")
        if row:
            movie_dict[row[2]] = {'score':int(row[1]), 'year':row[0]}
    print(movie_dict)
with open("deniro_json.txt", "w") as outfile:
    json.dump(movie_dict, outfile, indent = 4)