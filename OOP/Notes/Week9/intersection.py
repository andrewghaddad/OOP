# PC: Intersection
"""
Write a function that given two lists, returns a new list with only items
that appear in both lists
"""
def intersection(l1, l2):
    """
    IPO
    ([],[]) -> []
    """
    # for every value in the first list
    # check if that value is in the second list
    # if it is, then add it to the result list
    res = []
    for value in l1:
        if value in l2:
            res.append(value)
    return res

l = list(range(0,10,1)) # [0,1,2,3,4,5,6,7,8,9]
list_even = l[0:len(l):2] # [0,2,4,6,8]
list_odd = [0] + l[1:len(l):2] # [0,1,3,5,7,9]
l_intersect = intersection(list_even, list_odd)
print(l_intersect) # [0]