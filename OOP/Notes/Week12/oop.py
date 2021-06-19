# Introduction to Object Oriented Programming (OOP)
#   Classes, Properties, Instances
#   Constructors
#   Instance Methods

# OOP is a design paradigm that lets us "tightly couple" data elements together
# in order to better organize our code to solve more complicated problems

class Student():
    # description of our class
    # first_name = "pikachu" # first_name is a propery
    # last_name = "pokemon"

    # constructor function
    # this function runs one time when an object of the class is instantiated
    def __init__(self, fname, lname):
        print('A new student was instantiated')
        self.first_name = fname
        self.last_name = lname
        self.grades = []

    def say_hi(self):
        print("Hi, my name is ", self.first_name)

    def add_grade(self, grade):
        self.grades.append(grade)

    def compute_average(self):
        total = 0.0
        for grade in self.grades:
            total += grade
        try:
            average = total/len(self.grades)
        except:
            print("No grades found")
            return -1
        else:
            return average


student_1 = Student("pikachu", "pokemon") # creating an instance of our class
print(student_1)
print(student_1.first_name) # instance.property
print(student_1.last_name)

student_1.first_name = "bulbasaur" # updating property after instantiation
print(student_1.first_name)

student_2 = Student("charmander", "pokemon")
student_3 = Student("squirtle", "pokemon")
print(student_2.first_name)
print(student_3.first_name)

# instance methods
print()
student_1.say_hi() # instance.method()
student_2.say_hi()
student_3.say_hi()

# extend the student class to keep track of the grades a student receives
# in a course and add functionality to compute their average at any time
import random
for i in range(3):
    grade = random.randint(50, 100)
    print(grade)
    student_1.add_grade(grade)

average = student_1.compute_average()
print(average)