a= 4** 0.5
b= 42%6
c= "bat" < "bats"
d= format(3.14159, ".2f")
e= "Day" + "30"
f= "10" + "8" 
g= not (True != False)
h= bool(0) == False
i= print("")

print(a, b, c,d, e,f,g,h,i, sep="\n")


"""
problem 2:

((42 * z) / (x * ((x ** 2) + (y ** 3)))) ** 0.5

problem "finding second largest":

Idk if you need to use "for x in y", you could also do "for x in range(i, len(y)+1)", 
but then you'd need to replace x with a substring or a charAt

def secondLargest(string):
    largest=0
    second=0

    for x in string:
        num=int(x)
        if num > largest:
            largest= num
    for y in string:
        num=int(y)
        if num > second and num < largest:
            second =num

    return num 
"""
n=1
while n < 128: # print up to 64 but if has <= prints 128
    print(n)
    n *= 2

# compute average of three numbers
x = 10
y = 20
z = 30
result = (x + y + z) / 3
print("The result is " + str(result))

num=0
print("Before loop") # prints "before loop" and "after loop" but if has <= prints only "before loop"
while num < 0:
    num -= 1
print("After loop")


"""
print stars of triangle 

def pypart(n):
     
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ",end="")
      
        # ending line after each row
        print("\r")
 
# Driver Code
n = 5
pypart(n)
"""