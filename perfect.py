# date: 09/11/2019
# developer: Humphrey Shikoli
# programming language: Python
# description: program that calculates three-digit perfect number

import sys

if len(sys.argv) != 2:
    print("RuntimeError: pass one integer as the only argument")
    sys.exit()
    
arg_number = int(sys.argv[1])
lower_bound = 99
upper_bound = 999
isitperfect = 0

#############################################################################
# check whether the number entered is a 3-digit number
# if the number entered is a 3-digit number, find its divisors
# check whether the number suffices to be a perfect no.

if arg_number < lower_bound or arg_number == lower_bound or arg_number > upper_bound:
    print("Error: Please input a three digit number")
elif arg_number > lower_bound and arg_number < upper_bound or arg_number == upper_bound:
    for i in range(1, arg_number):
        if arg_number % i == 0:
            divisor = i
            isitperfect += divisor
    if isitperfect == arg_number:
        print(str(isitperfect) + " is a 3-digit perfect number")    
    else:
        print("The 3-digit number entered is not a perfect number")
