a, b = map(int, input().split())

count = 1

for i in range(10):
    a = a * 3
    b = b * 2

    if a > b:
        print(count)
        break
    else:
        count = count + 1

    i = i + 1
