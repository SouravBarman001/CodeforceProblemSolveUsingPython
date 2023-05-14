a = input().lower()
b = input().lower()

 # l = []
 # g = []
# convert to lowercase

# l = [x.lower() for x in c]
# g = [x.lower() for x in b]
# for i in range(0, len(c)):
#     l.append(c[i].lower())
#     g.append(b[i].lower())

# find ta ascii code of each char
# list1 = []
# list2 = []
# for i in range(0, len(c)):
#     list1.append(ord(a[i]))
#     list2.append(ord(g[i]))
# print(list1)
# print(list2)
# sumOne = 0
# sumTwo = 0
#
# for i in range(0, len(c)):
#     sumOne = list1[i] + sumOne

# print("sum One:", sumOne)
# l1 = sum(list1)
# l2 = sum(list2)
# print("sum of 1:", sum(list1))

if a < b:
    print('-1')
elif b < a:
    print('1')
else:
    print('0')
