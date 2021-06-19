# alphabetical sort
"""
input:
    two strings
processing:
    determine the order of the strings alpabetically
output:
    strings in alphabetical order

helper: .lower, .upper, len

"Banana"
"apple"
->
"apple"
"Banana"
"""
s1 = input("Please enter first string: ")
s2 = input("Please enter second string: ")

if s1.lower() < s2.lower():
    print(s1)
    print(s2)
else:
    print(s2)
    print(s1)