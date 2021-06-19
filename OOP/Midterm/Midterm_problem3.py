count = 0
largest=0
second=0

number = int(input("Please enter a positive integer: "))

while (number < 0):
    number = int(input("Please enter a positive integer: "))

while number > 1:
    if (number % 2):
        # n is odd
        number = 3*number + 1
        count = count + 1
        if number > largest:
            largest= number
        if number > second and number < largest:
            second =number
    if number ==0:
        break
    else:
        # n is even
        number = number//2
        count= count +1
        if number > largest:
            largest= number
        if number > second and number < largest:
            second =number
print("It took",count,"steps for the sequence to reach 1")
print("The largest number in the sequence was",largest,"(step = ",count,")")
print("The second largest number in the sequence was",second,"(step = ",count,")")