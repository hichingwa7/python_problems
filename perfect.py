# date: 09/11/2019
# developer: Humphrey Shikoli
# programming language: Python
# description: program that calculates three-digit perfect number

#############################################################################
#input is passed via the command line as one argument

import sys

if len(sys.argv) != 2:
    print("Error: pass one positive integer as the only argument")
    sys.exit()
    
arg_number = int(sys.argv[1])
lower_bound = 99
upper_bound = 999
isitperfect = 0
divisor = []

#############################################################################
# check whether the number entered is a 3-digit number
# if the number entered is a 3-digit number, find its divisors
# check whether the number suffices to be a perfect no.

if arg_number < lower_bound or arg_number == lower_bound or arg_number > upper_bound:
    print("Error: Please input a three digit positive integer")
elif arg_number > lower_bound and arg_number < upper_bound or arg_number == upper_bound:
    for i in range(1, arg_number):
        if arg_number % i == 0:
            divisor.append(i)
    isitperfect = sum(divisor)
    
    if isitperfect == arg_number:
        print(divisor, sep = '+', end = "")
        print(" = " + str(isitperfect))    
    else:
        print("The 3-digit number entered is not a perfect number")
