# PC: Reverse
"""
Write a function that returns the reverse of a string
reverse("hello") -> olleh
"""
def reverse(s):
    """
    IPO:
    (str) -> str
    """
    acc = ""
    for index in range(len(s)-1, -1, -1):
        ch = s[index]
        acc += ch
    return acc

def reverse2(s):
    """
    IPO:
    (str) -> str
    """
    acc = ""
    for index in range(len(s)):
        ch = s[index]
        acc = ch + acc
    return acc

print(reverse("hello"))
print(reverse2("hello"))

"""
PC: Palindrome tester

Write a function to determine if the a string is a palindrome
A palindrome is a string that reads the same forward and backwards

is_palindrome("racecar") -> True
    racecar
is_palindrome("apple") -> False
    elppa
"""
def is_palindrome(s):
    """
    IPO:
    (str) -> bool
    """
    reverse_s = reverse(s)
    return s == reverse_s

print(is_palindrome("racecar")) # True
print(is_palindrome("apple")) # False
