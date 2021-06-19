direction= input("Please enter a direction (l/r): ")
cols= int(input("Please enter an integer (>= 0): "))

if direction == "r":
    for i in range(1,cols):
        for j in range(i):
            print("", end=" ")
        for j in range(i, i+1):
            print(end="*")
        print()

    for i in range(cols ,0,-1):
        for j in range(i):
            print("", end=" ")
        for j in range(i, i+1):
            print(end="*")
        print()
elif direction == "l":
    for i in range(cols -1,0,-1):
        for j in range(i):
            print("", end=" ")
        for j in range(i, i+1):
            print(end="*")
        print()
    
    for i in range(0,cols):
        for j in range(i):
            print("", end=" ")
        for j in range(i, i+1):
            print(end="*")
        print()