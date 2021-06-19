# PC: Roulette
"""
Roulette is a game where a ball is rolled around in a circular track
eventually the ball will come to rest in a slot that is labelled with a number
between 0 and 36

Gamblers can bet on an individual number between 0 and 36.

Ask the user to enter a number.  Simulate spinning the roulette 1000 times.
Find out how many times the user's number comes up.

Extension: want to figure out which number appears the most and which appears the least
"""
import random

number = int(input("Please enter your guess: "))
frequency_counts = [0] * 37
# frequency_counts[i] stores the number of times the ball lands the number "i" 

for i in range(1000):
    random_number = random.randint(0, 36)
    frequency_counts[random_number] += 1

print(frequency_counts[number])
max_freq = max(frequency_counts)
min_freq = min(frequency_counts)
most_frequent_number = frequency_counts.index(max_freq)
least_frequent_number = frequency_counts.index(min_freq)
print(max_freq, most_frequent_number)
print(min_freq, least_frequent_number)
