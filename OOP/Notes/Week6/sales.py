# sales
"""
Write a program that asks the user for price values
When the user enters the word "end", you should stop asking for price prices
and display the following information:
    - the # of items purchased
    - their total price
    - 7% sales tax
    - their total bill w/ sales tax
    - the highest priced item and its item number
    - the lowest priced item and its item number
"""

# before
num_items = 0
total = 0.0
highest_price = 0
lowest_price = 0
highest_price_item_number = 0
lowest_price_item_number = 0
# during
while True:
    price = input("Please enter a price or 'end' to stop: ")
    if price == 'end':
        break
    price = float(price)
    num_items += 1
    if num_items == 1:
        # first iteration
        highest_price = price
        lowest_price = price
        highest_price_item_number = 1
        lowest_price_item_number = 1
    total += price
    if highest_price < price:
        highest_price = price
        highest_price_item_number = num_items
    if price < lowest_price:
        lowest_price = price
        lowest_price_item_number = num_items

# after
print("# of items:", num_items)
print("total:", format(total, ".2f"))
print("tax:", format(total*0.07, ".2f"))
print("total + tax:", format(total*1.07, ".2f"))
print("highest price + item number:", highest_price, highest_price_item_number)
print("lowest price + item number:", lowest_price, lowest_price_item_number)

