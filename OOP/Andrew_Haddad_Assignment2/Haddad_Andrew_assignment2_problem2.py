print("--------------------------------------------------------")

value1= float(input("Enter value 1: "))
value2= float(input("Enter value 2: "))


# ones 
ones_v1 = value1 % 10
ones_v2 = value2 % 10
print(ones_v1," + ",ones_v2," = ",ones_v1 + ones_v2, "one(s)")

# tens
tens_v1 = value1 % 100 // 10
tens_v2 = value2 % 100 // 10
print(tens_v1," + ",tens_v2," = ",tens_v1 + tens_v2, "tens(s)")

#hundreds
hund_v1 = value1 % 1000 // 100
hund_v2 = value2 % 1000 // 100
print(hund_v1," + ",hund_v2," = ",hund_v1 + hund_v2, "hundred(s)")

#thousands
thou_v1= value1 % 10000 // 1000
thou_v2= value2 % 10000 // 1000
print(thou_v1," + ",thou_v2," = ",thou_v1 + thou_v2, "thousand(s)")

print("--------------------------------------------------------")
