# PC: Pig Latin Translator
"""
Write a program that asks the user for a word
Translate the word into Pig Latin
Pig Latin can be generated using the following rules:
    - remove the first letter of the word
    - place the first letter at the end of the word
    - add the string "ay" to the end of the word

pig_latin_translator("hello") -> "ellohay"
"""

def pig_latin_translator(word):
    """
    IPO:
    (str) -> str
    """
    acc = ""
    for index in range(1, len(word)):
        ch = word[index]
        acc += ch
    if len(word) > 0:
        acc += word[0]
    acc += "ay"
    return acc

word = input("Please enter a word: ")
translated_word = pig_latin_translator(word)
print(translated_word)