"""
Write a function that takes a dictionary of strings to positive integers
Find the key associated with the largest integer value

{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
l
extension: return a list of keys if there is more than one key sharing the largest value
"""
def find_best_key(d):
    """
    I: 
        d: a dictionary of strings to positive integers
    P:
        find the keys with the largest value
    O:
        a list of keys
    ({str:int}) -> [str]
    """
    best_value = 0
    best_keys = []
    # find the best_value in d
    for key in d:
        value = d[key]
        if best_value < value:
            best_value = value
    # add all keys to output list that map to best_value
    for key in d:
        value = d[key]
        if value == best_value:
            best_keys.append(key)
    return best_keys

print(find_best_key({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 3, 'r': 3, 'd': 1})) # [l, w, r] 