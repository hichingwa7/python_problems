# date: 10/22/2019
# developer: Humphrey Shikoli
# programming language: Python
# description: program that uses a particular dataset (train.csv) and plots a  
# 2 x 2 plot showing how number of siblings/spouses or number of parents/children
# vary by age for both male and females

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("train.csv", quotechar = '"', skipinitialspace = True)
fig, axs = plt.subplots(2, 2, figsize = (7,7))
indexFemales = df[df['Sex'] == 'female'].index
df_1 = df.drop(indexFemales)
x_male = df_1["Age"]
y_male = df_1["SibSp"]
y_maleParch = df_1["Parch"]
indexMales = df[df['Sex'] == 'male'].index
df.drop(indexMales)
df_2 = df.drop(indexMales)
x_female = df_2["Age"]
y_female = df_2["SibSp"]
y_femaleParch = df_2["Parch"]
axs[0,0].scatter(x_male, y_male, marker = 'o', s = 5)
axs[0,0].set_xlim(-2,105)
axs[0,0].set_ylim(-0.5,5.5)
axs[0,0].set_xlabel("Age")
axs[0,0].set_ylabel("Number of Siblings/Spouses")
axs[0,0].set_title('Male SibSp')
axs[0,1].scatter(x_female, y_female, marker = 'o', s = 5)
axs[0,1].set_xlim(-2,105)
axs[0,1].set_ylim(-0.5,5.5)
axs[0,1].set_xlabel("Age")
axs[0,1].set_ylabel("Number of Siblings/Spouses")
axs[0,1].set_title('Female SibSp')

axs[1,0].scatter(x_male, y_maleParch, marker = 'o', s = 5)
axs[1,0].set_xlim(-2,105)
axs[1,0].set_ylim(-0.5,5.5)
axs[1,0].set_xlabel("Age")
axs[1,0].set_ylabel("Number of Parents/Children")
axs[1,0].set_title('Male Parch')
axs[1,1].scatter(x_female, y_femaleParch, marker = 'o', s = 5)
axs[1,1].set_xlim(-2,105)
axs[1,1].set_ylim(-0.5,5.5)
axs[1,1].set_xlabel("Age")
axs[1,1].set_ylabel("Number of Parents/Children")
axs[1,1].set_title('Female Parch')
plt.subplots_adjust(hspace = 0.5)
plt.show()
