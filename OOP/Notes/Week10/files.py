# .split
x = "name,occupation,affliation"
parts = x.split(",")
# (str) -> [str]
# splits a string into parts based on the argument passed in
print(parts) # ["name","occupation","affliation"]

"""
Given a file with format
name,value

Find the name with the corresponding largest value
Ask the user to enter the filename (could absolute/relative filename)
"""
filename = input("Please enter a filename: ")
file_object = open(filename, "r")
data = file_object.read()
lines = data.split("\n")

desired_name = ""
largest_value = -1
for line in lines:
    parts = line.split(",")
    name = parts[0]
    number = int(parts[1])
    if largest_value < number:
        largest_value = number
        desired_name = name

print(desired_name)
"""
    "r": read
    "w": write a new file/overwriting an existing
    "a": write a new file/append to an existing

    file_object.write("text here\nline2....")
"""