# date: 10/16/2019
# developer: Humphrey Shikoli
# programming language: Python
# description: program that reads in comma-separated file and stores the data in
# in a dataframe.

import pandas as pd

fileText = pd.read_csv("deniro.csv", quotechar = '"', skipinitialspace = True)
df = pd.DataFrame(fileText)
dfHeat = df[ df['Title'].str.contains('Heat')]
print(dfHeat)
print("\n")
dfYear = df[ df['Year'] == 1992]
print(dfYear)
