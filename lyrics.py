# date: 10/09/2019
# developer: Humphrey Shikoli
# programming language: Python
# description: program that reads in a number of textfiles and stores them in a 
# dictionary. Filenames are provided in the command line as arguments

import sys
data_dict = {}
data_dict_2 = {}
print(sys.argv[1:])

for songfile in sys.argv[1:]:
    title = ""
    with open(songfile) as infile:
        songtext = infile.readlines()
        thisisthefirstline = True
        for line in songtext:
            if thisisthefirstline:
                thisisthefirstline = False
                title = line
                continue
            words = line.split()
            for w in words:
                if w in data_dict:
                    data_dict[w] += 1
                else:
                    data_dict[w] = 1
                data_dict_2[w] = {'count':[w], 'songs':[title]}
        print(data_dict_2)
     

    
                    
                