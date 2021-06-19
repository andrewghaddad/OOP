
while True:
    time= int(input("Please enter the number of seconds elapsed: "))

    if time < 0:
        print("Exiting program...")
        break
    
    h= time/ 3600
    m= (time % 3600) / 60
    s= (time % 3600) % 60
    print(int(h),"hour, ",int(m),"minutes, ",s,"seconds")
