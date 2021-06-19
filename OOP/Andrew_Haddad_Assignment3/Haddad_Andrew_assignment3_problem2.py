print("Please enter three strings.")

s1= input("Enter the first string:  ")
s2= input("Enter the second string:  ")
s3= input("Enter the third string:  ")


if (s1.lower() < s2.lower()) and (s1.lower() < s3.lower()):
    print(s1)
    if s2.lower() < s3.lower():
        print(s2)
        print(s3)
    else:
        print(s3)
        print(s2)
elif (s2.lower() < s1.lower()) and (s2.lower() < s3.lower()):
    print(s2)
    if s1.lower() < s3.lower():
        print(s1)
        print(s3)
    else:
        print(s3)
        print(s1)
elif (s3.lower() < s2.lower()) and (s3.lower() < s1.lower()):
    print(s3)
    if s2.lower() < s1.lower():
        print(s2)
        print(s1)
    else:
        print(s1)
        print(s2)