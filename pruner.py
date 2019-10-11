# date: 10/09/2019
# developer: Humphrey Shikoli
# programming language: Python
# description: program that reads in a JSON file and stores in a dictionary and
# performs a number of manipulations on them

import json

babynames = {}
newdict = {}
babytext = {}
with open("baby_names.txt") as infile:
    babynames = json.load(infile)
print("\n")
    
for k, v in babynames.items():
    for i, j in v.items():
        newdict = {i:j for i,j in v.items() if i != 'Luke' and i != 'Aaron' and 
                   i != 'Avery' and i != 'Winston' and i != 'Gary' and j != '28'
                    and i.find('v') == -1 }
        newdict['Ron'] = 5
    babytext = {k:newdict}
print(babytext)

with open("better_names.txt", "w") as outfile:
    json.dump(babytext, outfile, indent = 4)
    
    