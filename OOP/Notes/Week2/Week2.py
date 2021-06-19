print("hello world")

# this is a single line comment
"""
This
is a 
multi line comment
"""

# IPO
# I: Input
# P: Processing
# O: Output

# Functions
"""
pre written piece of code that will perform a certain action
Python comes with many different in-built functions (e.g. print)
different functions take different number of arguments (e.g print take 0 or more arguments)
    - multiple arguments are separated by commas
        - print("hello", "world") # 2 arguments
    - print() # 0 arguments
calling a function means executing it
"""
print() # print newline, "\n"

# Data Types
"""
way of grouping together similar data
    - str (e.g. "hello world", 'name')
    - int (e.g. -3, -1, 0, 42, 1425)
    - float (e.g. -3.2, 0.53, 3.14, 3.0)
"""

# sep and end are two special arguments of print
# one*two
print("one*two")

print("one","two",sep="*")

print("one", end="*")
print("two")

print("one","two", sep = " ", end="\n")

# a,b,c
print("a", "b", "c", sep=",")

# variables
# variable_name = somedata
speed = 20
name = "shaheer"
name = "Shaheer"

print("The speed limit is", speed)

# naming a variable
"""
can't use reserved keywords (e.g. class, for, if)
cannot contain spaces
first character must be either a letter or an underscore
Python is case sensitive
"""

# class = 2, not legal
# class_avg = 124, legal
# classAvg = 99, legal
# _class_avg = 99, legal
# 2ndclassavg = 125, not legal
# classavg! = 99, not legal

# styling conditions
rockettopspeed = 1000
rocket_top_speed = 1000 # pothole or underscore case
rocketTopSpeed = 1000 # camelCase 

# reassigning variables
price = 12.99
print(price)
price = 10.99
print(price)
print()


# Item: Bread, Price: $ 2.99
# Item: Eggs, Price: $ 1.99
prod_name1 = "Bread"
prod_price1 = 2.99
prod_name2 = "Eggs"
prod_price2 = 1.99
print("Item: ", prod_name1, ", Price: $ ", prod_price1, sep="")
print("Item: ", prod_name2, ", Price: $ ", prod_price2, sep="")

# Data Input
# we have learned how to
#   STORE
#   OUTPUT
# however the data was always hardcoded

# input
# in-built function
# takes 0 or 1 argument
# reads an input from the user until "ENTER" is pressed
# returns a str

user_age = input("Please enter an age: ")
print("The user entered: ", user_age)
print()

# math operators
# +, -, *, /
print(2+2) # 4
print(42-2) # 40
print(10*5) # 50
print(24/5) # 4.8