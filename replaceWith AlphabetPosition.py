""""
 given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

example: 

alphabet_position("The sunset sets at twelve o' clock.")

result => "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

"""

import string

# Average approach
def alphabet_position(text):
    d = {L: str(i) for i, L in enumerate('abcdefghijklmnopqrstuvwxyz', 1)}

    result = ''
    for t in text.lower():
        result += d.get(t, t)

    print(result)
    

# Best Approach

def alphabet_position2(text):
    alphabeths = {v: k for k, v in enumerate(string.ascii_lowercase, start=1)}
    return " ".join(str(alphabeths.get(char)) for char in text.lower() if char in alphabeths.keys())

print(alphabet_position2("The sunset sets"))