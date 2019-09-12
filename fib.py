# Date: 09/11/2019
# Developer: Humphrey Shikoli
# Programming Language: Python
# Description: program that finds fibonacci number without using recursion


import sys

#argv = n;

if len(sys.argv) != 2:
    print("RuntimeError: pass one integer as the only argument")
    sys.exit()

arg_number = int(sys.argv[1])

#Assume Fibonacci series starts with 0 followed by 1
#Function finds the nth fibonacci no.
#After fibonacci one, a fibonacci no. is found by adding two no.s before it

def fibonacci(arg_number):
    x = 0
    y = 1
    if arg_number < 0:
        print ("Fibonacci for the number does not exist")
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
    
