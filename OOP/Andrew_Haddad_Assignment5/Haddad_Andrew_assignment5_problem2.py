students = int(input("How many students are in your class?" ))

while students<0:
    print("Invalid # of students, try again.")
    students = int(input("How many students are in your class?" ))

tests = int(input("How many tests in this class? "))

while tests < 0:
    print("Invalid # of tests, try again.")
    tests = int(input("How many tests in this class? "))
print("Here we go!")

class_average = []

for i in range(1, students+1):
    student_marks = []
    print("**** Student #",i, "****")
    for j in range(1,tests+1):
        marks = int(input("Enter score for test #{}: ".format(j)))
        while marks<0:
            print("Invalid score, try again")
            marks = int(input("Enter score for test #{}: ".format(j)))
        student_marks.append(marks)
    student_average = sum(student_marks) / len(student_marks)
    rounded_average = round(student_average, 3)
    print("Average score for student #", i, "is ", rounded_average)
    class_average.append(rounded_average)

whole_class_average = sum(class_average) / len(class_average)

rounded_class_average = round(whole_class_average, 2)
print("Average score for all students is: ", rounded_class_average)