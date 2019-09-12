# date: 09/11/2019
# developer: Humphrey Shikoli
# programming Language: Python
# description: program that converts from F to C with F ranging from 0 to 300 in steps of 20 degrees

step_up = 20
upper_bound = 301
temp_f = 0
temp_c = 0
temp_const1 = 32
temp_const2 = 5/9
degree_sign = u'\N{DEGREE SIGN}' #unicode encoding for the degree sign

#####################################################################################################
# iterate the given range in steps of 20 degrees
# convert the F temperature to C temperature using the given formula
# output all the F temperatures with their respective C temperatures rounded off to 2-decimal places

for i in range(upper_bound):
    if i % step_up == 0:
        temp_f = i
        temp_c = (temp_f - temp_const1) * temp_const2 
        print (str(temp_f) + degree_sign + "F" + " = " + "{0:.2f}".format(temp_c) + degree_sign + "C")
