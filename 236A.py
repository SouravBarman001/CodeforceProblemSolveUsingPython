input_string = input()

convertToSet = set(input_string)

totalLength = len(convertToSet)

if totalLength % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
