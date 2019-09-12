# date: 09/11/2019
# developer: Humphrey Shikoli
# programming language: Python
# description: program that prints multiples of 5, 7 or 13 between 0 and 101

###########################################################################################

factor5 = 5
factor7 = 7
factor13 = 13
lower_bound = 0
upper_bound = 101

############################################################################################
# for loop iterates over the numbers between 0 to 101
# if statements check whether current no. under iteration range is a multiple of 5,7 or 13

for x in range(lower_bound,upper_bound):
    if x % factor5 == 0 and x % factor7 == 0 and x % factor13 == 0 and x != 0:
        print(str(x) + " is a multiple of " + str(factor5) + " and " + str(factor7) + " and " + str(factor13) + "!")
    elif x % factor5 == 0 and x % factor7 == 0 and x % factor13 != 0 and x != 0:
        print(str(x) + " is a multiple of " + str(factor5) + " and " + str(factor7) + "!")
    elif x % factor5 == 0 and x % factor7 != 0 and x % factor13 != 0 and x != 0:
        print(str(x) + " is a multiple of " + str(factor5) + "!")
    elif x % factor5 != 0 and x % factor7 == 0 and x % factor13 == 0 and x != 0 :
        print(str(x) + " is a multiple of " + str(factor7) + " and " + str(factor13) + "!")
    elif x % factor5 != 0 and x % factor7 == 0 and x % factor13 != 0 and x != 0:
        print(str(x) + " is a multiple of " + str(factor7) + "!")
    elif x % factor5 == 0 and x % factor7 != 0 and x % factor13 == 0 and x !=0 :
        print(str(x) + " is a multiple of " + str(factor5) + " and " + str(factor13) + "!")
    elif x % factor5 != 0 and x % factor7 != 0 and x % factor13 == 0 and x != 0:
        print(str(x) + " is a multiple of " + str(factor13) + "!")

    
