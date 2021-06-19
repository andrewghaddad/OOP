

while True:
    cols= int(input("How many columns? "))
    if cols > 0:
        break

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