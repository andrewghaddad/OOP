# for loop
"""
for VAR_NAME in ITEMS:
    statement(s)

range(start, end, step)
range(start, end) # step = 1
range(end) # start = 0, step = 1

range(start, end, step)
    returns [start, start + step, start + 2*step, ..., end)

range(5) = [0, 1, 2, 3, 4]
range(0,10,2) = [0,2,4,6,8]
range(10,0,-1) = [10,9,8,7,6,5,4,3,2,1]
"""

for i in range(5):
    print(i)