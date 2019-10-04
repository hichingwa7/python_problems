# date: 09/30/2019
# developer: Humphrey Shikoli
# programming language: Python
# description: program that takes a single positive integer as input from  the command
# line and checks if the number is odd, a palindrome, a factorial, a square number or
# if all the digits in the number are in increasing order

import sys

if len(sys.argv) != 2:
    print("Error: pass one integer as the only argument")
    sys.exit()

def isOdd(n):
    numodd = n
    if numodd % 2 == 1:
        return True
    else:
        return False
        
def isSquare(n):
    if n == 1:
        return True
    numsquare = n // 2
    squareset = set([numsquare])
    while numsquare * numsquare != n:
        numsquare = (numsquare + (n // numsquare)) // 2
        if numsquare in squareset:
            return False
        squareset.add(numsquare)
    return True
    
def isIncreasing(n):
    numinc = str(n)
    numlen = len(numinc)
    count = 0
    while count < numlen:
        if numlen == 1:
            return True
        if numlen > 1 and numinc[count] < numinc[(count + 1)]:
            return True
        else:
            return False
        count += 1
    
def isPalindrome(n):
    numpal = str(n)
    numrev = str(numpal[::-1])
    if numrev == numpal:
        return True
    else:
        return False
    
def isFactorial(n):
    num = 1
    numfactorial = n
    factnum = 1
    while factnum < numfactorial:
        num = num + 1
        factnum = factnum * num
    if factnum == numfactorial:
        return True
    else:
        return False
    
if isOdd(int(sys.argv[1])) == True:
    print("\n")
    print("The number {0}".format(int(sys.argv[1])) +" is odd")
    print("\n")
else:
    print("\n")
    print("The number {0}".format(int(sys.argv[1])) +" is not odd")
    print("\n")
if isSquare(int(sys.argv[1])) == True:
    print("The number {0}".format(int(sys.argv[1])) +" is a square number")
    print("\n")
else:
    print("The number {0}".format(int(sys.argv[1])) +" is not a square number")
    print("\n")
if isIncreasing(int(sys.argv[1])) == True:
    print("The number {0}".format(int(sys.argv[1])) +" is increasing")
    print("\n")
else:
    print("The number {0}".format(int(sys.argv[1])) +" is not increasing")
    print("\n")
if isPalindrome(int(sys.argv[1])) == True:
    print("The number {0}".format(int(sys.argv[1])) +" is a palindrome")
    print("\n")
else:
    print("The number {0}".format(int(sys.argv[1])) +" is not a palindrome")
    print("\n")

if isFactorial(int(sys.argv[1])) == True:
    print("The number {0}".format(int(sys.argv[1])) +" is a factorial")
else:
    print("The number {0}".format(int(sys.argv[1])) +" is not a factorial")
    