import re

inputString = input()

x = re.findall("[A-Z]", inputString)
y = re.findall("[a-z]", inputString)

if len(x) < len(y) or len(x) == len(y):
    print(inputString.lower())
elif len(x) > len(y):
    print(inputString.upper())
