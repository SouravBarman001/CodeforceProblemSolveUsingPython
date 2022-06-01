n = int(input())

all = [int(i) for i in input().split()]
count = 0
for i in range(len(all)):
    if all[i] == 1:
        count = count + 1

if count == 0:
    print("EASY")
else:
    print("HARD")
