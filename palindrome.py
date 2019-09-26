# date: 09/25/2019
# developer: Humphrey Shikoli
# programming language: Python
# description: program that outputs 7-digit palindromes that are square numbers

###############################################################################

upperbound = 10000000
lowerbound = 1000000

###############################################################################
# squarenumber() function utilizes babylonian algorithm to check whether a number
# is a perfect square or not and returns a boolean value to the calling program. 

def squarenumber(z):
    x = z // 2
    y = set([x])
    while x * x != z:
        x = (x + (z // x)) // 2
        if x in y:
            return False
        y.add(x)
    return True

###############################################################################
for i in range(lowerbound, upperbound):
    j = str(i)
    if squarenumber(int(j)) == True:
        if j[0] == j[-1] and j[1] == j[-2] and j[2] == j[-3]:
            print(j +" is a palindrome")