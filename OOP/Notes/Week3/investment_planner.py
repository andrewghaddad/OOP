# Investment Planner
"""
F = P(1+r)^n

P is the present value
F is the future value
r is the rate of return
n is the number of years
Given F, r, and n, calculate P

P = F/(1+r)^n
"""
# Input
F = float(input("Please enter desired future value: "))
r = float(input("Please enter annual rate of return: "))
n = int(input("Please enter how many years you would like to invest for: "))


# Processing
P = F / (1+r)**n

# Output
print("To have", F, "in", n, "years, you would need to invest", format(P, ".2f"), "today")
