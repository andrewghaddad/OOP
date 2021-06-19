print("GRADE CALCULATOR")
print("-----------------------------------------------------------------------")


a1= float(input("Enter the student’s grade on Assignment #1: "))
a2= float(input("Enter the student’s grade on Assignment #2: "))
a3= float(input("Enter the student’s grade on Assignment #3: "))
quiz= float(input("Enter the student’s grade on the weekly quizzes component: "))
midterm= float(input("Enter the student’s midterm grade: "))
final= float(input("Enter the students final exam grade: "))
avg_grade= (a1+a2+a3) / 3
print("Average assignment grade: ",avg_grade)
print("/n")
final_grade= (((a1 + a2 + a3) / 3) * .25)+ (quiz * .05)+ (midterm * .25)+ (final * .45)
print("Final Grade: ", format(final_grade, ".1f"))

print("Is it an A? ",bool(final_grade >= 95.0))