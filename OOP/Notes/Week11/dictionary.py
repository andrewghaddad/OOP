# a collection of (key, value) pairs
"""
Mon -> Monday
Tues -> Tuesday
...


"""
# how to create a dictionary
d = {} # vs l = []

# store values in a dictionary
# d[key] = value # adding to a list : .append(value) or l += [value]
d["a"] = 96 # ("a", 96)
d["b"] = 98 # ("b", 98)
d["z"] = 122 # ("z", 122)

# l[i] = new_value # updates value at l[i] to be new_value
d["a"] = 97 # overwrite the existing value associated with key = "a"

# How to get values from a dictionary
v = d["a"]
print(v) # 97

# trying to get a value using a non-existant key results in a runtime error
# we can also the in operator to check if a key exists in the dictionary
# ("c" in d) would return True if "c" is a key in d, otherwise False
try:
    v = d["c"]
except:
    print("c is not a key in d")
else:
    print(v)

# deleting values in a dictionary
del d["a"] # ("a", 97) from d
try:
    v = d["a"]
except:
    print("a is not a key in d")
else:
    print(v)

print()
# how to iterate over a dictionary
# (b, 98)
# (z, 122)
for key in d:
    value = d[key]
    print("key =", key, "value =", value)

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

"""
    the keys in a dictionary have to be unique, but the values don't have to be
    the keys in a dictionary must be immutable
    sometimes we may want to use a list or another mutable data type as a key
    the trick is we represent the list as a string, then we use it as a key
    [1,2,1] -> "[1,2,3]" 
"""