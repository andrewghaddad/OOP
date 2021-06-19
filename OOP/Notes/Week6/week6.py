# while loops
"""
while condition(s):
    statement(s)

1. Write code to complete a task once
2. Place that code into a loop
3. Write a condition to exit the loop
4. Double check your work
    a) before the loop
    b) during the loop
    c) after the loop

Do we need a while a loop to solve the following problems?

1. Ask the user for two numbers, then print their product
    - ans: no
    follow up: we only want to accept positive numbers
        - ans: yes
    while number <= 0:
        number = int(input("..."))
        if number <= 0:
            print("Invalid input!")

2. Ask the user to enter 5 price values, output the total + 7% sales tax
    ans: no
    follow up: what if the user could enter an unlimited number of items
        ans: yes
"""