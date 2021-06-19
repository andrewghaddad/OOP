sentinel = -1

# accumulator variable
total = 0
count = 0

while True:
    weight = int(input("Enter your weight: "))
    if weight == sentinel:
        break
    last_number = weight
    if count == 0:
        first_number = weight
    total += weight
    count += 1
    

if count > 0:
    print("Average Weight Over",count,"Days: ",total/count)
    print("Total Weight Loss Over",count,"Days: ",first_number- last_number)
else:
    print("No valid weight was entered")