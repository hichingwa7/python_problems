# date: 10/14/2019
# developer: Humphrey Shikoli
# programming language: Python
# description: program that reads in a number of textfiles and stores them in a 
# JSON file and stores it in a pandas dataframe.

import pandas as pd

fileDict = {}
fileName = []
fileCount = []
fileNameDict = {}
fileCountDict = {}
newdict = {}
babytext = {}
fileText = pd.read_json("baby_names.txt")
fileLen = len(fileText)
for k,v in fileText.items():
    for i,j in v.items():
        fileName.append(i)
        fileNameDict = fileName
        fileCount.append(j)
        fileCountDict = fileCount
        fileDict = {'Name':fileNameDict, 'Count':fileCountDict}
df = pd.DataFrame(fileDict)        
indexCount = df[df['Count'] == 28].index
df.drop(indexCount, inplace = True)
indexAaron = df[df['Name'] == 'Aaron'].index
df.drop(indexAaron, inplace = True)
indexLuke = df[df['Name'] == 'Luke'].index
df.drop(indexLuke, inplace = True)
indexAvery = df[df['Name'] == 'Avery'].index
df.drop(indexAvery, inplace = True)
indexWinston = df[df['Name'] == 'Winston'].index
df.drop(indexWinston, inplace = True)
indexGary = df[df['Name'] == 'Gary'].index
df.drop(indexGary, inplace = True)
sub = 'v'
indexV = df[ df['Name'].str.find(sub) == 2 ].index
df.drop(indexV, inplace = True)
df =  df.append({'Name': 'Ron', 'Count': 5}, ignore_index = True)
df = pd.DataFrame(df.reset_index(drop = True))
print(df)