a, b = map(int, input().split())

r = a * b
count = 0

if r % 2 != 0:
    for i in range(1, r):
        if i % 2 == 0:
            count += 1
        else:
            pass
else:
    for i in range(0, r):
        if i % 2 == 0:
            count += 1
        else:
            pass

print(count)
