# date : 08/04/2022
num = int(input())
textElement = input()
count = 0
for i in range(0, len(textElement) - 1):
    if textElement[i] == textElement[i + 1]:
        count += 1
    else:
        continue


print(count)
