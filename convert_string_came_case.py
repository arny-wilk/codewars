"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
"""

import re

def to_camel_case(text):
    if text != '':
        text_space = re.sub(r"[-!$%^&*()_+|~=`{}\[\]:\";'<>?,.\/]", " ", text)
        if text_space.lower() and text_space.capitalize():
            output = ''.join(x for x in text_space.title() if x.isalnum())
            return output[0].lower() + output[1:]
        elif text_space.title():
            output = ''.join(x for x in text_space if x.isalnum())
            return output[0].lower() + output[1:]
            return text_space
    else :
        return text

print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case("the stealth warrior"))
print(to_camel_case("A-B-C"))
