n, k = map(int, input().split())

remainder = 0
for i in range(k):
    remainder = n % 10

    if remainder == 0:
        n = n / 10
    else:
        n -= 1
print(int(n))
