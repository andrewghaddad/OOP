x = list(input("Enter scores: ").split()) #taking multiple inputs from user

temp = [] #empty list
sume = 0
score = 0
for i in x: #loop in entered list
    if i.isdigit() == True: #validate data in list
        sume = sume+int(i) #addup valid score
        score = score+1 #count number of scores
        temp.append(int(i)) #valid score append to new list
        print("Adding Score: ",i)
    else:
        print("Invalid score: ",i)

print()# print all statistics
print("Total Score: ",score)
print("Maximum Score: ",max(temp))
print("Miniimum Score: ",min(temp))
print("Average Score",sume/score)