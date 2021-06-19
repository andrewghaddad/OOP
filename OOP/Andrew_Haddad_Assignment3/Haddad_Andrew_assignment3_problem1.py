print("Valid Triangle Tester")

# Point 1 inputs
point1_x= float(input("Enter Point #1 - x position: "))
point1_y= float(input("Enter Point #1 - y position: "))

# Point 2 inputs
point2_x= float(input("Enter Point #2 - x position: "))
point2_y= float(input("Enter Point #2 - y position: "))

# Point 3 inputs
point3_x= float(input("Enter Point #3 - x position: "))
point3_y= float(input("Enter Point #3 - y position: "))

print("The length of each side of your test shape is:")

# lengths of each sides
side1_length= ((point2_x - point1_x)**2)+((point2_y - point1_y)**2)
side2_length= ((point3_x - point2_x)**2)+((point3_y - point2_y)**2)
side3_length= ((point3_x - point1_x)**2)+((point3_y - point1_y)**2)

print("Side 1: ", side1_length)
print("Side 2: ", side2_length)
print("Side 3: ", side3_length)

"""
(a) Side 1 + Side 2 must be longer than Side 3
(b) Side 2 + Side 3 must be longer than Side 1
(c) Side 3 + Side 1 must be longer than Side 2

"""

# if trangle is valid or not
if side1_length + side2_length > side3_length :
    print("This is a valid triangle!")
elif side2_length + side3_length > side1_length :
    print("This is a valid triangle!")
elif side3_length + side1_length > side2_length :
    print("This is a valid triangle!")
else:
    print("This is not a valid triangle.")

#if triangle is isosceles, equilateral, or scalene

if side1_length and side2_length == side3_length:
    print("This is an equilateral triangle")
elif side1_length or side2_length == side3_length:
    print("This is an isosceles triangle")
else:
    print("This is an scalene triangle")


