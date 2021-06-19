# Generate a random integer in the range [1,10]
# Ask the user to guess the number until they guess correctly

import random
play = ""
while play != "no":
    lower_bound = 1
    upper_bound = 10
    secret_number = random.randint(lower_bound, upper_bound)
    guess = 0
    while True:
        guess = int(input("Please enter your guess: "))
        if guess == secret_number:
            print("Congratulations!")
            break
        else:
            if guess < secret_number:
                print("Your guess was too low")
            else:
                print("Your guess was too high")
    play = input("Do you want to keep playing? Enter 'no' to stop: ")
# 1. Write code to solve the problem once
# 2. Place the code into a loop
# 3. Figure out the exit condition
# 4. Double check your work
#   a) check before the loop
#   b) check during the loop
#   c) check  after the loop