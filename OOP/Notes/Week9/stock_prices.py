# PC: Stock Prices
"""
Write a program that asks the user for daily closing stock Prices
Store these values in a list and print them out at the end of the program

The user can indicate when they are finished entering prices by entering a negative number.
Your program shouldn't print the negative number at the end
"""
price = 0
l = []
while price >= 0:
    price = float(input("Please enter a value: "))
    l += [price]

l = l[0:len(l)-1]

for p in l:
    print(p)
