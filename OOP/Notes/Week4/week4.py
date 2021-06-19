# Decision structures and boolean logic
# so far our programs have been deterministic and sequential

a = 5
b = 10
print(a > b and a > 1) # False
print(a > 1 and b > a) # True
print(a == 5 and b < 100) # True
print(a > 1 and b < 1 and b < a) # False
print(a > 1 and b > 1 and b < a) # False

print(a > b or a > 1) # True
print(a > 1 or b > a) # True
print(a == 5 or b < 100) # True
print(a > 1 or b < 1 or b < a) # True
print(a > 1 or b > 1 or b < a) # True

print(not True) # False
print(not False) # True

print(4 < 2) # False
print(not (4 < 2)) # True
print(not (not (4 < 2))) # False
print()


# String comparison (ascii)
print("dog < cat =", "dog" < "cat") # False
print("fish < alligator =", "fish" < "alligator") # False
print("elephant == tiger =", "elephant"=="tiger") # False
print("bat != honey badger =", "bat" != "honey badger") # True
print("bat > bank =", "bat" > "bank") # True 
print("bat < bats =", "bat" < "bats") # True
print("Z < a =", "Z" < "a") # True
# the ascii values for all upper case letters is less than the ascii values
# for all lower case letters ("Z" < "a")
# within the same, the ascii values are sorted in alphabetical order ("A" < "Z")

# string manipulation
# .lower, .upper
apple = "Apple"
print(apple.lower())
print(apple.upper())

# len
# counts the number of characters in a string
print(len(apple)) # 5