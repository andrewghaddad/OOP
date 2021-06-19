# length sort
"""
input:
    two strings
processing:
    determining the order of strings based on their length
output:
    shorter string followed by longer string

bowl
pan
->
pan
bowl
"""
s1 = input("Please enter first string: ")
s2 = input("Please enter second string: ")

if len(s1) < len(s2):
    print(s1)
    print(s2)
else:
    print(s2)
    print(s1)