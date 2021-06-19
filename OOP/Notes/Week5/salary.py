"""
3 employees
Compute the salary for each employee given
    - commission rate
    - sales
"""
counter = 0
num_loops = 3
while counter < num_loops:
    rate = float(input("Please enter commission rate: "))
    sales = float(input("Please enter sales: "))
    salary = rate * sales
    print("Employee " + str(counter + 1) + "'s salary is " + format(salary, ".2f"))
    counter += 1 # counter = counter + 1

# 1. Write code to solve the problem once
# 2. Place the code into a loop
# 3. Figure out the exit condition
# 4. Double check your work
#   a) check before the loop
#   b) check during the loop
#   c) check  after the loop