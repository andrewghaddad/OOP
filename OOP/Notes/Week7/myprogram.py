# importing
"""
the import statement tells Python to load the functions that exist
within a specific module into memory
and make them available to use

(import random to use random.randint function)

Because you don't see the inner workings of a function inside of a module,
we sometimes call them "black boxes"

A "black box" describes a mechanism that accepts input
and performs an operation that can't be seen using that input
and produces some kind of output
"""

# creating your own module
"""
Create a new Python script (e.g. myfunctions.py)
Place your function defintions inside this script
Create new Python script (e.g. myprogram.py)
Import your function module using the import statement in myprogram.py
    import myfunctions
Call your functions using the dot notation
    myfunctions.function1()
    myfunctions.does_something_else(arg1, arg2)
"""

"""
Create a module called geometry_helper
Write two functions in this module
    - area_of_circle
    - circumference_of_circle
Each function takes on argument (the radius) and returns the result
Assume that pi = 3.14
"""
import geometry_helper
radius = float(input("Please enter a radius: "))
area = geometry_helper.area_of_circle(radius)
circumference = geometry_helper.circumference_of_circle(radius)
print(area, circumference)