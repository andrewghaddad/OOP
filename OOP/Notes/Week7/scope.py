"""
def bugs():
    numbugs = int(input("How many bugs: "))
    return numbugs

bugs()
print(numbugs)
"""

# the code above results in a runtime error because
# 'numbugs' is only visible inside the local scope of the 'bugs' function

# scope refers to the region where a variable is visible
# every function has it's own local scope

def change_me(v): # v = 10
    print("function got: ", v)
    v = 10
    print("argument is now: ", v)

my_var = 5
print("starting with:", my_var)
change_me(my_var)
print('ending with:', my_var)
