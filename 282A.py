# count = 0
# n = int(input())
#
# for i in range(n):
#
from past.builtins import raw_input

n = 0
for i in range(int(input())):
    k = raw_input()
    if k[0] == '+' or k[1] == '+':
        n += 1
    else:
        n -= 1
print(n)
