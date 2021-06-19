# generate 3 numbers
# for each number ask the user to enter a lower bound and an upper bound
# generate a random number between the two bounds
# at the end, print out the 3 numbers separated by a -
# e.g. "42-3-16"
import random
# random_number = random.randint(lower_bound, upper_bound)

acc = ""
for i in range(3):  
    lower_bound = int(input("Please enter a lower bound: "))
    upper_bound = int(input("Please enter a upper bound: "))
    random_number = random.randint(lower_bound, upper_bound)
    if i == 2:
        acc += str(random_number)
    else:
        acc += str(random_number) + "-"

print(acc)