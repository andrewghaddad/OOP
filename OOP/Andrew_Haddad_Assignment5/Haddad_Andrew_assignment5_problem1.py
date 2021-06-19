budget = int(input("Enter budget for your party: "))
cost_slice = float(input("Cost per slice of pizza: "))
cost_pie = float(input("Cost for whole pizza pie(8 slices): "))
people = int(input("How may people attending your party? "))

sum1 = 0
sliices = 0
pies = 0
total_cost = 0.0
for i in range(1,people+1):
    person_slices = int(input("Enter number of slices for person #"+str(i)+": "))
    
    if person_slices > 0:
        sum1 = sum1 + person_slices
        
    else:
        while(person_slices < 0):
            print("Not a valid entry, try again!")
            person_slices = int(input("Enter number of slices for person #"+str(i)+": "))
        sum1 = sum1 + person_slices          
    
pies = int(sum1 / 8)
slices = sum1 % 8
total_cost = ((cost_pie * pies) + (slices * cost_slice))
print("You should purchase "+str(pies)+" pies and "+str(slices)+" slices")
print("Your total cost will be: "+str(total_cost))
balance = budget - total_cost

if balance > 0:
    print("You still have "+str(balance)+" left after your order")
if balance < 0:
    balance = balance * (-1)
    print("This would put you over budget by "+str(balance))
if balance == 0:
    print("You will have no money left after your order.")
    