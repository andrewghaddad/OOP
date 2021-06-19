"""
prime checker
given a number
determine if the number is prime
a number is prime if and only if, the only divisors the number has are 1 and itself
"""

num_divisors = 0
number = int(input("Please enter a number: "))
d = 1
while d <= number:
    if number % d == 0:
        num_divisors += 1
    d += 1

if num_divisors == 2:
    print(number, "is prime!")
else:
    print(number, "is not prime.")

# 1. Write code to solve the problem once
# 2. Place the code into a loop
# 3. Figure out the exit condition
# 4. Double check your work
#   a) check before the loop
#   b) check during the loop
#   c) check  after the loop