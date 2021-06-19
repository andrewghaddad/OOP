# PC: Overtime Pay Calculator
"""
Input:
    number of hours
    hourly rate
Processing:
    if hours <= 40: total = hours * rate
    o/w: for every worked after 40, the rate is 1.5x
Output:
    total pay
"""

hours = int(input("Please enter number of hours: "))
rate = float(input("Please enter hourly rate: "))

total_pay = hours * rate
if hours > 40:
    total_pay = (hours-40)*(1.5*rate) + 40*rate

print(format(total_pay, ".2f"))

"""
if condition(s):
    statement(s)
"""

"""
math operator:
    +,-,*,/,//,%,**
relation/comparison operator:
    <, >, <=, >=, ==, !=
    e.g. a < 5
assignment operator:
    =
logical operator:
    and, or, not
    e.g. 
        a < 5 and a > 0
        not True

"""