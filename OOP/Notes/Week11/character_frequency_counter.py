"""
Write a function that takes in a string and returns a dictionary
where each key is a character in the string and the corresponding value
is the number of times the character appears in the string

"hello world"
{
    "h":1,
    "e":1,
    "l":3,
    "o":2,
    " ":1,
    "w":1,
    "r":1,
    "d":1
}
"""
def freq_counter(s):
    """
    I:
        s: a string
    P:
        build a dictionary where the keys are characters in s and the corresponding
        values are the number of times each character appears in s
    O:
        return the dictionary
    (str) -> {str:int}
    """
    d = {}
    # go through each character
    for ch in s:
    # for each character
    # check if the character is already in the dictionary or not
        if ch in d:
    #   if it is:
    #       update its current count
            d[ch] += 1
        else:
    #   otherwise:
    #       we should add it to the dictionary
            d[ch] = 1
    return d

print(freq_counter("hello world"))