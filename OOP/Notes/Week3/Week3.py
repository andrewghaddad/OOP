# Data Types
# str (textual data)
# int (integers)
# float (floating point numbers)
# bool (True/False)

# 5, int
# 5.5, float
# "Hello", str
# Hello, variable
# "5.5", str
# 2.975, float
# 2.0, float
# True, bool
# false, variable

num_1 = 5
num_1 = 4.99
# num_1 = $5,124.99 # syntax error
# Python is dynamically typed (vs statically typed)
# this means that we do not need to declare 
# the data types of our variables

# User Input and Math expressions
# Recall the 'input' function
# it returns a str
# need a way to convert between data types
#   - int(), float(), str()
#   - the above functions take 1 argument
my_num = int(input("Please enter a number: "))
print(my_num, type(my_num))#
print(10 - my_num)
print(10/my_num)

# Errors, Bugs, and Debugging

# Types of Errors

"""
    Syntax Errors:
        The code does not follow the rules of the language
        e.g.
            starting a string with a single quote, but ending with a double quote
            mismatching parenthesis

    Runtime Errors:
        The code is syntactically correct, however the program may crash while running 
        e.g. 
            dividing by 0
            trying to convert a value to a data type that doesn't make sense ("hello" to int)

    Logical Errors:
        Arguably the hardest to debug
        The program is syntactically correct and does not crash while running
        however the actual output differs from the expected output
        e.g.
            (a + b + c) / 3 vs a + b + c / 3
"""

# Math operators
# +, -, *, /, //, %, **
print("2 ** 4 =", 2 ** 4) # 16
print("5 / 2 =", 5 / 2) # 2.5
print("43 // 8 =", 43 // 8) # 5
print("43 % 8 =", 43 % 8) # 3

# Escape characters
# - interpret the following character in a "special" way
# the escape character in Python is \
# \n, \t, \', \", \\
print('Hi I\'m shaheer')
print("line1\t2line2\nline3")