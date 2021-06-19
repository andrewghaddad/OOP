"""
Pick a secret number between 1 and 10 (hard code to be 7)
Input:
    ask the user to enter a number between 1 and 10
Processing:
    if the user is correct:
        print congratulations
    if the user's guess is too low:
        print appropriate message
    if the user's guess is too high:
        print appropriate message
Output:
    message from processing
"""
secret_number = 7

user_guess = int(input("Please enter your guess: "))
if secret_number == user_guess:
    print("Congratulations!")
else:
    if user_guess < secret_number:
        print("Your guess was too low!")
    else:
        print("Your guess was too high!")
