def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 == 1

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def is_perfect(number):
    factor_sum = 0
    for i in range(1, number):
        if number%i == 0:
            factor_sum += i
    return factor_sum == number

def is_abundant(number):
    factor_sum = 0
    for i in range(1, number):
        if number%i == 0:
            factor_sum += i
    return number < factor_sum

print("\n"+"Main Menu"+"\n")

print("1 - Find all prime numbers within a given range")
print("2 - Find all perfect numbers within a given range")
print("3 - Find all abundant numbers within a given range")
print("4 - Chart all even, odd, prime, perfect and abundant numbers within a given range")
print("5 - Quit")

choice = int(input("/n"+"Your choice: "))

if (choice > 5 or choice < 1):
    print("Invalid, try again")

def get():
    start = int(input("Enter starting number (positive only): "))
    while (start< 0):
        print("Invalid, try again")
        start=int(input("Enter starting number (positive only): "))
    end=int(input("Enter ending number: "))
    while (end < start):
        print("Invalid, try again")
        end = int(input("Enter ending number: "))
    return (start, end)

while choice != 5:
    a, b = get()

    if choice == 1:
        print(f"\nAll prime numbers between {a} and {b}")
        print("#"*20)

        for i in range(a, b+1):
            if is_prime(i):
                print(i)

        print("#"*20)
    elif choice == 2:
        print(f"\nAll perfect numbers between {a} and {b}")
        print("#"*20)

        for i in range(a, b+1):
            if is_perfect(i):
                print(i)

        print("#"*20)
    elif choice == 3:
        print(f"\nAll abundant numbers between {a} and {b}")
        print("#"*20)

        for i in range(a, b+1):
            if is_abundant(i):
                print(i)

        print("#"*20)
    elif choice == 4:
        print(f"\nAll prime numbers between {a} and {b}")
        print("#"*20)

        for i in range(a, b+1):
            if is_prime(i):
                print(i)

        print("#"*20)
        print(f"\nAll perfect numbers between {a} and {b}")
        print("#"*20)

        for i in range(a, b+1):
            if is_perfect(i):
                print(i)

        print("#"*20)
        print(f"\nAll abundant numbers between {a} and {b}")
        print("#"*20)

        for i in range(a, b+1):
            if is_abundant(i):
                print(i)
                
        print("#"*20)

