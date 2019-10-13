# date: 10/09/2019
# developer: Humphrey Shikoli
# programming language: Python
# description: program that reads in a number of textfiles and stores them in a 
# dictionary. Filenames are provided in the command line as arguments

import sys
import json

file_list = []
words = []
unique_words = []
file_dict = {}
final_dict = {}

textdict = []

argvlen = len(sys.argv) - 1
if argvlen < 2:
    print("Pass atleast one textfile at the command line argument")

position = 1
try:
    while position <= argvlen:
        print(argvlen)
        with open(sys.argv[position], 'r') as infile:
            textdict.append(sys.argv[position])
        position += 1
except IndexError:
    sys.exit

for each_file in textdict:
    
    with open(each_file, "r+") as infile:
        file_data = infile.readlines()
        thisisthefirstline = True
        endoffile = False
    for line in file_data:
        if thisisthefirstline:
            thisisthefirstline = False
            continue
        file_data_1 = line.split(" ")
        for n in file_data_1:
            
            words.append(n)

for w in words:
    if w not in unique_words:
        unique_words.append(w)

for each_word in unique_words:
    count = words.count(each_word)
    song_list = []
    for each_file in textdict:
        with open(each_file, "r+") as current_file:
            file_data_1 = current_file.read().split()
            if each_word in file_data_1:
                song_list.append(each_file)

    final_dict.update({each_word.lower(): {"Count": count, "Songs": song_list}})

print(final_dict)
with open("lyrics_json_1_songs.txt", 'w') as outfile:
    json.dump(final_dict,outfile, indent = 4)