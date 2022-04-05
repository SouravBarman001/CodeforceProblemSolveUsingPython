n = int(input())
count = 0
for i in range(0, n):
    x, y, z = input().split()
    a = int(x)
    b = int(y)
    c = int(z)
    if a+b == 2 or b+c == 2 or a+c == 2:
        count += 1
print(count)
