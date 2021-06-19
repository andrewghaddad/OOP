# Exceptions
"""
try:
    # questionable code
    print("hello ")
    y = 5 / 1
    print("world")
except:
    # runs only if the try block encounters a runtime error
    print("An error occurred!")
else:
    # runs only if the try block does not encounter a runtime error
    print("No error!")
finally:
    # runs no matter what
    print("Finally")
"""

"""
Ask the user for a test score and the total number of points possible on a test.
Ensure the test score is non-negative and a valid floating point number.
Ensure the total points entered is non-negative and a valid floating point number.
Generate the test average.  Make sure you don't divide by 0.
If that happens, then print an appropriate message to the user.
"""
while True:
    try:
        test_score = float(input("Please enter a test score: "))
    except:
        print("Please enter a floating point number.")
    else:
        if test_score >= 0:
            break
        else:
            print("Please enter a non-negative number.")

while True:
    try:
        total_points = float(input("Please enter total points possible: "))
    except:
        print("Please enter a floating point number.")
    else:
        if total_points >= 0:
            break
        else:
            print("Please enter a non-negative number.")

try:
    average = test_score / total_points
except:
    print("Total points should be greater than 0.")
else:
    print(average)