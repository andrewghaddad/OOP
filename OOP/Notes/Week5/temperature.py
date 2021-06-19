"""
Write a program that given a temperature in Farenheit
Output the temperature in Celsius (rounded to 2 decimal places)
continue to ask the user for temperatures until they enter 'no'
C = 5/9 * (F - 32)
"""
temperature = ""
while temperature != "no":
    temperature = input("Please enter a temperature or 'no' to stop: ")
    if temperature == 'no':
        break
    else:
        celsius = (float(temperature) - 32) * 5/9
        print(format(celsius, ".2f"))

# 1. Write code to solve the problem once
# 2. Place the code into a loop
# 3. Figure out the exit condition
# 4. Double check your work
#   a) check before the loop
#   b) check during the loop
#   c) check  after the loop