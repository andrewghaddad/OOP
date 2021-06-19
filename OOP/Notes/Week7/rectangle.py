# rectangle
"""
Write a program that prints the following pattern using
user defined function(s)

**********
*        *
*        *
*        *
*        *
**********

c = "*", w = 10, h = 6

user defined function syntax
def function_name(arg1, arg2, ...):
    statement(s)
"""
def solid_line(ch, width):
    print(ch * width)

def hollow_line(ch, width):
    print(ch, ch, sep= " "*(width-2))

def print_rectangle(ch, width, height):
    solid_line(ch, width)
    for i in range(height - 2):
        hollow_line(ch, width)
    solid_line(ch, width)

c = input("Please enter a character to use: ")
w = int(input("Please enter a width: "))
h = int(input("Please enter a height: "))

print_rectangle(c, w, h)