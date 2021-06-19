# PC: grades
"""
Write a function that given a list of grades, a lower bound, and an upper bound
counts the number of grades in between the lower and upper bound
use the function to count the number of As, Bs, Cs, Ds, and Fs in the given list
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: <60
"""
grades = [90, 100, 70, 45, 76, 85, 93, 21, 36, 99, 100]
def count_letter_grades(grades, lower, upper):
    """
    I:
        grades: a list of values
        lower: a lower bound
        upper: an upper bound
    P:
        count the number of values in grades that are between lower and upper
    O:
        return the count we compute
    ([float], float, float) -> int
    """
    count = 0
    for value in grades:
        if lower <= value <= upper:
            count += 1
    return count

print(count_letter_grades(grades, 90, 100)) # 5
print(count_letter_grades(grades, 80, 89)) # 1
print(count_letter_grades(grades, 70, 79)) # 2
print(count_letter_grades(grades, 60, 69)) # 0
print(count_letter_grades(grades, 0, 60)) # 3