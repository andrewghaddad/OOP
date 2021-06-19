# grades
"""
ask the user to enter grades until they enter -1
compute the average of all the grades entered
"""

# sentinel
sentinel = -1

# accumulator variable
total = 0
count = 0

while True:
    grade = int(input("Please enter a grade: "))
    if grade == sentinel:
        break
    last_number = grade
    if count == 0:
        first_number = grade
    total += grade
    count += 1
    

if count > 0:
    print("first:",first_number)
    print("last:",last_number)
    print(total/count)
else:
    print("No valid grades were entered")
# 1. Write code to solve the problem once
# 2. Place the code into a loop
# 3. Figure out the exit condition
# 4. Double check your work
#   a) check before the loop
#   b) check during the loop
#   c) check  after the loop