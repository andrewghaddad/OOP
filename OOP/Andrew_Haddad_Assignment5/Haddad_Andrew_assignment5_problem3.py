start_num = int(input("Start number :  "))
end_num = int(input("End number :  "))
line = 0

for num in range(start_num, end_num + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           count = 0
           n = num
           while (n > 0):
               count = count + 1
               n = n // 10
           num = str(num)
           line += 1
           print(num+((10-count)*" "),end='')
           if (line%10 == 0):
               print("\n")