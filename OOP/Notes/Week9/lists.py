# list basics

# A list is used to hold multiple values using a single variable identifier
# you can create a list using the square brackets
l = [] # l = list() 
l = [1,2,3]
str_list = ["apple", "banana"]
mixed_list = [1, "two", False, 4.0, 5]
print(l, str_list, mixed_list, sep="\n")
print()
# list concatenation and list repetition
my_list = [1,2] + [100] # "ab" + "c" = "abc"
print(my_list) # [1,2,100]
my_list = [1,2] * 3 # "a" * 5 = "aaaaa"
print(my_list) # [1,2,1,2,1,2]
print()

# indexing elements in a list
print(my_list[0]) # 1
# lists are mutable (unlike strings!)
# s[0] = 'h' # this was an error because strings are immutable
my_list[0] = "a"
print(my_list)

# list mechanics (referencing list variables)
x = 3
y = x
x = 4
print(x, y) # 4 3
l1 = [1,2,3]
l2 = l1
l1[0] = 100
print(l1, l2, sep='\t')

# how to copy a list
l3 = [] + l1
l3[0] = 0
l2[0] = "a"
print(l1, l2, l3, sep="\t")
print()

# iterating over a list
my_list = [1,2,3,4]
for element in my_list:
    print(element, end = " ")
print()

for i in range(len(my_list)):
    print(my_list[i], end=" ")
print()
print()

# creating new lists
my_list = []
my_list = [0] * 7 # [0,0,0,0,0,0,0]
my_list = list(range(9,-1,-1)) # [9,8,7,6,5,4,3,2,1,0]
print(my_list)

# adding to a list
value = 100
my_list = my_list + [value]
print(my_list)

# slicing a list
start = 0
end = len(my_list)
new_list = my_list[start:end:2] # slicing creates a new list
print(my_list, new_list) # [9, 7, 5, 3, 1, 100]

# we can use the 'in' operator to check if a value exists in a list
num = 10
if num in new_list:
    print("Found!")
else:
    print("Not found!")
print()

# list functions
my_list = []
print(my_list)
# append
my_list.append(5)
print(my_list)
# remove
my_list.remove(5)
print(my_list)
# sort
my_list = list(range(9, -1, -1)) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(my_list)
my_list.sort()
print(my_list)
# reverse
my_list.reverse()
print(my_list)
# index
ind = my_list.index(3)
print(ind) # 6
# my_list.index(10) would result in an error because 10 is not in my_list
# max/min
max_value = max(my_list) # 9
min_value = min(my_list) # 0
index_of_max = my_list.index(max_value) # 0
index_of_min = my_list.index(min_value) # 9
print(max_value, index_of_max) # 9, 0
print(min_value, index_of_min) # 0, 9
