# Character counter
"""
Write a function that accepts two arguments
a string and a single character
count the number of times the character appears in the string

counter("hello", 'l') -> 2
counter('hello', 'x') -> 0
"""
def counter(s, ch):
    """
    IPO:
    (str, str) -> int
    """
    acc = 0
    for index in range(len(s)):
        curr_ch = s[index]
        if curr_ch == ch:
            acc += 1
    return acc

print(counter("hello", 'l')) # 2
print(counter("hello", 'x')) # 0

# Vowel counter
"""
Write two functions to count the number of vowels in a string
The first function should use the counter function we implemented above
The second functions shouldn't use the counter function or the in-built count function
"""
def count_vowels_version1(s):
    """
    IPO
    (str) -> int
    """
    acc = 0
    vowels = "aeiouAEIOU"
    for ch in vowels:
        acc += counter(s, ch)
    return acc


def count_vowels_version2(s):
    """
    IPO
    (str) -> int
    """
    acc = 0
    for index in range(len(s)):
        curr_ch = s[index]
        if curr_ch == 'a' or curr_ch == 'A' or curr_ch == 'e' or curr_ch == 'E' or curr_ch == 'i' or curr_ch == 'I' or curr_ch == 'o' or curr_ch == 'O' or curr_ch == 'u' or curr_ch == 'U':
            acc += 1
    return acc

print(count_vowels_version1("hello wOrld")) # 3
print(count_vowels_version2("hello wOrld")) # 3
