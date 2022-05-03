tramStop = int(input())

p = 0
max = 0
for i in range(tramStop):

    a, b = map(int, input().split())

    p = b - a + p
    if max < p:
        max = p

print(max)