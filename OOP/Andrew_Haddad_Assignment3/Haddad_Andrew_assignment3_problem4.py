print("Enter a date in YYYYMMDD format:")

date= int(input("Enter start date MMDDYYYY:  "))

date_year= date % 10000 
date_day= date % 1000000 // 10000
date_month= date % 100000000 // 1000000

if (date_month == 1 or 3 or 5 or 7 or 9 or 11) and (date_day == 30):
    print("That's not a valid date!")
elif (date_month == 2 or 4 or 6 or 8 or 10 or 12) and (date_day == 31):
    print("That's not a valid date!")
elif date_month > 12:
    print("That's not a valid date!")
elif (date_month == 2) and (date_day > 28):
    print("That's not a valid date!")
elif (date_month < 9) and (date_year < 2020):
    print("This date is before the semester begins")
elif (date_month > 12) and (date_day < 21) and (date_year >= 2020):
    print("This date is after the semester")
elif (date_year > 2020):
    print("This date is after the semester")
elif (date_month == 9) and (date_day == 3 or 8 or 10 or 15 or 17 or 22 or 24 or 29):
    print("You have class today")
elif (date_month == 10) and (date_day == 1 or 6 or 8 or 13 or 15 or 20 or 22 or 27 or 29):
    print("You have class today")
elif (date_month == 11) and (date_day == 3 or 5 or 10 or 12 or 17 or 19 or 24):
    print("You have class today")
elif (date_month == 12) and (date_day == 1 or 3 or 8 or 10):
    print("You have class today")
else:
    print("You do not have class today")
