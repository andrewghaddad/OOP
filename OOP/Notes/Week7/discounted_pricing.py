# Discounted Pricing
"""
Prompt the user for an item price (using a function)
Apply a 20% discount to the price (using a function)
Print the starting price and the discounted price

extension:
    don't accept price values < 0.05 and > 100
    repeat until the user elects to stop by entering "stop"

def function_name(arg1, arg2, ...):
    statement(s)

return
    - used to save values computed in a function, by assigning the function call to a variable
        e.g. z = sum_two(x, y)
    - a function immediately exits when it hits a 'return' statement
"""

def get_user_input(prompt, lower_bound, upper_bound):
    """
    I:
        prompt: the text to display to the user
        lower_bound: the minimum value price has to be greater than
        upper_bound: the maximum value price has to be less than
    P: 
        to prompt the user for price value
    O:
        return the price value
    (str, float, float) -> float
    """
    while True:
        price = float(input(prompt))
        if price > lower_bound and price < upper_bound:
            break
        else:
            print("Invalid price!")
    return price

def apply_discount(price, discount_percentage):
    """
    I: 
        price: the value to be discounted
        discount_percentage: the percent to discount
    P:
        apply the given discount to the price
    O:
        return the discounted price
    (float, float) -> float
    """
    return (1 - discount_percentage) * price


def sum_two(x, y):
    return (x + y)

while True:
    price = get_user_input("Please enter a price: ", 0.05, 100)
    print("starting price =", format(price, ".2f"))
    discounted_price = apply_discount(price, 0.2)
    print("discountd price =", format(discounted_price, ".2f"))
    user_choice = input("Please enter 'stop' to end: ")
    if user_choice == "stop":
        break