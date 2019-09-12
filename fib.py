# date: 09/11/2019
# developer: Humphrey Shikoli
# programming language: Python
# description: program that finds fibonacci number without using recursion

import sys

#argv = n;

if len(sys.argv) != 2:
    print("RuntimeError: pass one integer as the only argument")
    sys.exit()

arg_number = int(sys.argv[1])

##########################################################################
# assume Fibonacci series starts with 0 followed by 1
# function finds the nth fibonacci no.
# after fibonacci one, a fibonacci no. is found by adding two no.s before it

def fibonacci(arg_number):
    x = 0
    y = 1
    if arg_number < 0:
        return ("Fibonacci for the number entered does not exist")
    elif arg_number == 0:
        return x
    elif arg_number == 1:
        return y

    else:
        for i in range(2,arg_number+1):
            z = x + y
            x = y
            y = z
        return z
            
print(fibonacci(arg_number))
    
