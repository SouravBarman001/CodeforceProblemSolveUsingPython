import re

inputInteger = int(input())
charValue = input().upper()

x = re.findall('[A]', charValue)
y = re.findall('[D]', charValue)

countA = x.count('A')
countB = y.count('D')

if countA > countB:
    print('Anton')
elif  countA == countB:
    print('Friendship')
else:
    print('Danik')
