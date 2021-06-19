# Coins
"""
Ask the user for
    pennies
    nickels
    dimes
    quarters
Output the amount of change they have
"""
# Input
pennies = int(input("How many pennies? "))
nickels = int(input("How many nickels? "))
dimes = int(input("How many dimes? "))
quarters = int(input("How many quarters? "))

# Processing
total = 0.01*pennies + 0.05*nickels + 0.1*dimes + 0.25*quarters

# Output
print("total change =", format(total, ".2f"))

# format(variable, ".2f")