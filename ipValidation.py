'''
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
IPs should be considered valid if they consist of four octets,
with values between 0 and 255, inclusive.

Examples of valid inputs:
1.2.3.4
123.45.67.89

Invalid input examples:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089

'''

import re

def is_valid_IP(string):
    listString = string.split('.')
    if len(listString) == 4:
        return True

    for element in listString:
        regex = r'^([1-9]\d*|0)$'
        if element == re.match(regex, element):
            return True

        if 0 <= int(element) <= 255:
            return True

    return False


print("A list of test for the function is_valid_IP : ")
print(is_valid_IP('12.255.56.1'))
print(is_valid_IP(''))
print(is_valid_IP('abc.def.ghi.jkl'))
print(is_valid_IP('123.456.789.0'))
print(is_valid_IP('12.34.56'))
print(is_valid_IP('12.34.56 .1'))
print(is_valid_IP('12.34.56.-1'))
print(is_valid_IP('123.045.067.089'))
print(is_valid_IP('127.1.1.0'))
print(is_valid_IP('0.0.0.0'))
print(is_valid_IP('0.34.82.53'))
print(is_valid_IP('192.168.1.300'))
