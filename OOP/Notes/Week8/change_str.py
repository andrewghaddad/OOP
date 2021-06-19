# PC: Changing a str
"""
Write a function that accepts three arguments
a string, a character, and a replacement character
replace all occurrences of character with the replacement character
return the new string

change_str("hallo", "a", "e") -> "hello"

cannot do something like the following
if string[index] == 'a':
    string[index] == 'e' # we cannot do this b/c strings are immutable
"""
def change_str(s, old_ch, new_ch):
    """
    IPO:
    (str, str, str) -> str
    """
    acc = ""
    for index in range(len(s)):
        ch = s[index]
        if ch == old_ch:
            acc += new_ch
        else:
            acc += ch
    return acc

print(change_str("hallo", "a", "e"))