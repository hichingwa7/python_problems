# date: 10/01/2019
# developer: Humphrey Shikoli
# programming language: Python
# description: program that takes two words as input from the command line and
# performs a number of operations on them

import sys

if len(sys.argv) != 3:
    print("Error: Pass two words as the only arguments")
    sys.exit()

def spellBackwards(word1):
    x = word1
    xrev = x[::-1]
    print("\n")
    print("The reverse of {0} is {1}".format(x, xrev))
    return xrev 
    
def capitalize(word2):
    x = word2
    xupper = x.upper()
    print("The capital of {0} is {1}".format(x, xupper))
    return xupper
    
def threadTogether(word1, word2):
    strthread = []
    x = word1
    y = word2
    xcalled = str(spellBackwards(x))
    ycalled = str(capitalize(y))
    xlen = len(xcalled)
    ylen = len(ycalled)
    wordslen = xlen + ylen
    offset = 0
    for i in range(wordslen):
        if offset < xlen:
            strthread.append(xcalled[i])
        if offset < ylen:
            strthread.append(ycalled[i])
        offset += 1
    print("Threaded, they become ", *strthread, sep = '')

def printItOut(x, y):
    arg1 = x
    arg2 = y
    threadTogether(arg1, arg2)
    
printItOut(str(sys.argv[1]), str(sys.argv[2]))