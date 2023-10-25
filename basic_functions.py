#!/usr/bin/env python3
#basic_functions.py

#multiply.py
def multiply(a,b):
    return a*b
    """ This function will will multiply the 2 numbers 
    given as input and will return the value of the
    multiplication """

x=multiply(10,100)
print("The value of x is {}".format(x))

#hello_name.py
def hello_name(name="you"):
        print("Hello, {}!".format(name))
        """ This function will return any name that
        is inputted, and will just return "Hello, You!"
        if no name is inputted """
hello_name()

#less_than_ten.py
def less_than_ten(list):
    """ This function will take a list of numbers
    and will return a list of numbers less than 10 """
    number_list = []
    for i in list:
        if i < 10:
            number_list.append(i)
    return number_list
number_list1 = less_than_ten([8, 6, 1, 9, 10, 87, 22, 112, 3])
print(number_list1)
