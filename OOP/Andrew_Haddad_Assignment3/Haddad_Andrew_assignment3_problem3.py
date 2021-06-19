print("Instructions: Enter the start date and birthdate for an employee to determine their age at the start of employment")

start_date= int(input("Enter start date MMDDYYYY:  "))
birth_date= int(input("Enter birth date MMDDYYYY:  "))

birth_year= birth_date % 10000 
birth_day= birth_date % 1000000 // 10000
birth_month= birth_date % 100000000 // 1000000
# print(birth_year)
# print(birth_day)
# print(birth_month)

start_year= start_date % 10000 
start_day= start_date % 1000000 // 10000
start_month= start_date % 100000000 // 1000000



if birth_month == 9:
    b_month= "September"
if birth_month == 10:
    b_month= "October"
if birth_month == 11:
    b_month= "November"
if birth_month == 12:
    b_month= "December"
if birth_month == 1:
    b_month= "January"
if birth_month == 2:
    b_month= "Feburary"
if birth_month == 3:
    b_month= "March"
if birth_month == 4:
    b_month= "April"
if birth_month == 5:
    b_month= "May"
if birth_month == 6:
    b_month= "June"
if birth_month == 7:
    b_month= "July"
if birth_month == 8:
    b_month= "August"


if (birth_day % 10) == 1:
    day_suffix= "th"
if (birth_day % 10) == 2:
    day_suffix= "nd"
if (birth_day % 10) == 3:
    day_suffix= "rd"

print("The contestant was born on",b_month,birth_day,day_suffix,",",birth_year)

if (start_year - birth_year) > 21:
    print("ELIGIBLE: The contestant will be 21 by the time taping begins")
elif (start_year - birth_year) > 21:
    print("NOT ELIGIBLE: The contestant won't be 21 by the time taping begins")
elif birth_date == start_date:
    print("ELIGIBLE: The contestant will be 21 by the time taping begins")
elif (start_year - birth_year) == 21:
    if (start_month < birth_month):
        print("NOT ELIGIBLE: The contestant won't be 21 by the time taping begins")
    elif (start_month > birth_month):
        print("ELIGIBLE: The contestant will be 21 by the time taping begins")
    elif (start_month == birth_month):
        if (start_day < birth_day):
            print("NOT ELIGIBLE: The contestant won't be 21 by the time taping begins")
        elif (start_day > birth_day): 
            print("ELIGIBLE: The contestant will be 21 by the time taping begins")
        elif (start_day == birth_day):
            print("ELIGIBLE: The contestant will be 21 by the time taping begins")