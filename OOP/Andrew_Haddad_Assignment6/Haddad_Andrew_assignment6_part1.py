n= int(input("Select number to test up until: "))

while(n < 0):
    n= int(input("Select number to test up until: "))

prime_list= ["P" for i in range(n+1)]

prime_list[0]='N'
prime_list[1]='N'


if n <=800:
    for i in range(2,n+1):
        if prime_list[i]=='N': 
            continue
        mult=2*i
        while mult<= n:
            prime_list[mult]='N' 
            mult +=i 

    count= 0
    for i in range(n+1):
        if prime_list[i]=='P':
            print(i,end='\t')
            count=(count+1)%10
            if count==0: 
                print() 
else:
    for i in range(2,800+1):
        if prime_list[i]=='N': 
            continue
        mult=2*i
        while mult<= n:
            prime_list[mult]='N' 
            mult +=i 

    count= 0
    for i in range(800+1):
        if prime_list[i]=='P':
            print(i,end='\t')
            count=(count+1)%10
            if count==0: 
                print() 

