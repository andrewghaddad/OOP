# String manipulation
"""
String is a data type
String is a sequence of characters
    e.g. "hello"
    e.g. ""
    e.g. "a"

ASCII Table
    0-9: 48-57
    A-Z: 65-90
    a-z: 97-122

ord(char) -> ascii_value (e.g. ord('a') returns 97)
chr(ascii_value) -> char (e.g. chr(97) returns 'a')

chr(ord('a')) -> chr(97) -> 'a'

first = "asljfadsfal"
second = "29048502"
third = "LJDLKASJFLAJFAL"
second, third, first

string indexing
an index is a position in the string

"hello"
 01234

s = "hello"
zeroth_character = s[0]
last_character = s[4] # s[len(s)-1], s[-1]

iterating over a string:

for ch in s:
    # statement(s)

for index in range(len(s)):
    ch = s[index]
    # statement(s)

functions/methods
    - len()
    - upper()
    - lower()
    - chr()
    - ord()
    - isalpha()
        returns True is all the characters in a string are alphatical
        "apple".isalpha() returns True
        "var0".isalpha() returns False
    - isalnum()
        returns True is all the characters in a string are alphanumeric
    - isspace()
        returns True is all the characters in a string are spaces
    - find()
        s.find(substr, start_index)
        returns the starting index of the specified substr in s
        returns -1 if not found

        the second argument 'start_index' specifies where to start looking

        s = "hello world"
        print(s.find("world", 0)) # 6
        print(s.find("world", 7)) # -1
    - count()
        s.count(ch)
        counts the number of times ch appears in s
    - in operator
        - substr in s
            if "shaheer" in s:
                # True is "shaheer" appears as a substr in s
            else:
                # "shaheer" is not a substr in s
    - replace()
        s.replace(old_str, new_str)
        replaces all the occurrences of old_str with new_str
        "hello".replace('l', 'x') -> 'hexxo'
"""
