# primes
"""
Write a program that determines if a number is prime
Print out all the prime numbers between 1 and 10000
2
...
9973
extension: print only 10 numbers per line
extension: align the rows evenly
"""
count = 0
max_length = len(str(9973)) # get number of digits in 9973
for n in range(1, 10001):
    # checks if n is prime
    num_divisors = 0
    for factor in range(1, n+1):
        if n % factor == 0:
            # factor is a divisor of n
            num_divisors += 1
    if num_divisors == 2:
        num_digits = len(str(n)) # number of digits n has
        num_spaces = max_length - num_digits
        print((" " * num_spaces) + str(n), end=" ") # n is prime
        count += 1
        if count == 10:
            print()
            count = 0