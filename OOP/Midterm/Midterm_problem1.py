n1= 0
n2= 1
count = 0
fib_string=""
fib_num = int(input("Please enter a non-negative integer: "))
    
while (fib_num < 0):
    print("Not a valid entry, try again!")
    fib_num = int(input("Please enter a non-negative integer: "))


while count < fib_num:
    fib_string += str(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
print(fib_string, sep=",")

cont= input("Do you wish to continue? ")

if cont == "yes":
    fib_num = int(input("Please enter a non-negative integer: "))
    while count < fib_num:
        fib_string += str(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    print(fib_string, sep=",")

if cont == "no":
    print("Finished!")