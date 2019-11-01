# date: 10/22/2019
# developer: Humphrey Shikoli
# programming language: Python
# description: program that uses a particular dataset (train.csv) and bins how many people 
# survived for each gender in 10-year blocks

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("train.csv", quotechar = '"', skipinitialspace = True)
df.drop(['Cabin'], axis = 1, inplace = True)
df.dropna(inplace = True)
df1 = df[df["Survived"] == 1]
df2 = df1[["Survived","Age", "Sex"]]
interval = [x for x in range(0,100,10)]
ageLabel = [10, 20, 30, 40, 50, 60, 70, 80, 90]
df2["Age_bins"] = pd.cut(x = df2["Age"], bins = interval, right = False, labels = ageLabel)

maleCount = []
femaleCount = []

maleSurvived = df2[df2["Sex"] == "male"].index
femaleSurvived = df2[df2["Sex"] == "female"].index
df_male = df2.drop(femaleSurvived)
df_female = df2.drop(maleSurvived)
x_maleBins = df_male["Age_bins"]
x_femaleBins = df_female["Age_bins"]

for elem in x_maleBins:
    maleCount.append(elem)
maleAgeBin = pd.Series(maleCount)
m_counts = maleAgeBin.value_counts()

for elem in x_femaleBins:
    femaleCount.append(elem)
femaleAgeBin = pd.Series(femaleCount)
f_counts = femaleAgeBin.value_counts()

fig = plt.subplots(figsize = (5.5,5.5))
width = 2.7
plt.bar([elem - width + 2 for elem in m_counts.index], m_counts, width, label = "Male")
plt.bar([elem + 1.7 for elem in f_counts.index], f_counts, width, label = "Females")
plt.xticks(range(0,105,10))
plt.ylabel("Count")
plt.xlabel("Age")
plt.title("Survival by Age and Gender")
plt.legend(loc = 'best')
plt.show()