# date: 09/24/2019
# developer: Humphrey Shikoli
# programming language: Python
# description: program that reads a file and drops every second alphanumeric character

######################################################################################
# open the given file and store the read string in the variable "givenstr"

with open("caractacus.txt") as f:
    givenstr = f.read()

# empty string variable that will store the new manipulated string
b = ""

#the orders variable is a list that stores numbers in the range specified
orders = list(range(44,58))
orders += list(range(65,91))
orders += list(range(97,123))
orders += list(range(3,14))
count = 0

# write into a new textfile, "trimmed.txt", following the if conditions specified
# The "ord()" function accepts a string of length one and returns its unicode point
# representation and if that value is in the "orders" list, it is checked if it is 
# not divisible by two and ignored, else the value is added in the "b" string variable

with open ("trimmed.txt", "w") as newstr:
    for i in givenstr:
        if i == " " or i == "\r" or i == "," or i == "\n" or i == "'":
            b += i
        else:
            if ord(i) in orders:
                if count % 2 == 1:
                    pass
                else:
                    b += i
                count += 1
                
    print(b)
    newstr.write(b)