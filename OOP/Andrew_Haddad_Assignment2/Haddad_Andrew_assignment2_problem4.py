value= float(input("Enter value: "))
rounded_num= int(value)
print(rounded_num)


"""

1.) value= input(float("Enter value: ")) --> would cause syntax error becuase i switched the float and input functions
2.) value= float(input(Enter value: )) --> would cause syntax error becuase i forgot the "" around the input message
3.) rounded_num= int(value) --> would cause logical error becuase it could not round the decimal correctly 
4.) value= input("Enter value: ") --> would cause runtime error becuase i could not convert str to int
5.) value= int(input("Enter value: ")) --> would cause runtime error becuase it would not take input of a decial

"""
