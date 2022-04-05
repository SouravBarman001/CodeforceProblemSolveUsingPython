a, b = map(int, input().split())

arr = [int(i) for i in input().split()]
pos = arr[b - 1]
count = 0
length = len(arr)
for i in range(0, length):
    if arr[i] >= pos and arr[i] > 0:
        count += 1

print(count)
