import random

while True:
    dice= int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))
    if dice == 4 or dice == 6 or dice == 8 or dice == 10 or dice == 12 or dice == 20:
        print("Thanks! Here we go ...")
        break
    

total1 = 0
count1 = 0
total2 = 0
count2 = 0
double_count= 0

lower_bound = 1
upper_bound = dice

die1= random.randint(lower_bound, upper_bound)
die2= random.randint(lower_bound, upper_bound)

while True:
    if die1== 1 and die2==1:
        print("You got snake eyes! Finally! On try number ", count1)
        break
    if die1 == die2:
        double_count += 1
    die1= random.randint(lower_bound, upper_bound)
    die2= random.randint(lower_bound, upper_bound)
    print("die number 1 is",die1,"and die number 2 is",die2)
    total1 += die1
    count1 += 1
    total2 += die2
    count2 += 1

doubles= count1/double_count * 10
if count1 and count2 > 0:
    print("Along the way you rolled doubles",double_count, "times (",doubles,"of all rolls were doubles)")
    print("The average roll for die #1 was",format(total1/count1, ".2f"))
    print("The average roll for die #2 was",format(total2/count2, ".2f"))