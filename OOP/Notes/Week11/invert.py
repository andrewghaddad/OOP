"""
Write a function that takes in a dictionary of strings to integers
invert the dictionary

you should return a new dictionary, where the old values are now keys and
the old keys are now values in the new dictionary

Be careful, the keys in a dictionary are unique, but the values may not be, so
we use a list of values for each in the inverted dictionary

{str:int} -> {int:[str]}

d = {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 3, 'r': 3, 'd': 1}
invert_d = {
    1: ["h", "e", " ", "d"],
    2: ["o"],
    3: ["l", "w", "r"]
}
l = invert_d[key]
l.append(v)
"""
def invert(d):
    """
    I:
        d: a dictionary of str to int
    P:
        build a new dictionary where the new keys are the old values
        and the new values are the old keys
    O:
        the new dictionary
    ({str:int}) -> {int:[str]}
    """
    invert_d = {}
    for key in d:
        value = d[key]
        if value in invert_d:
            l = invert_d[value]
            l.append(key)
        else:
            invert_d[value] = [key]
    return invert_d

d = {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 3, 'r': 3, 'd': 1}
print(invert(d))