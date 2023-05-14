k, n, w = map(int, input().split())

totalCost = 0
ithValue = []

for i in range(1, w + 1):
    totalCost = i * k
    ithValue.append(totalCost)

sumOfTotal = sum(ithValue)

if n == sumOfTotal or n > sumOfTotal:
    print(0)

else:
    borrow = sumOfTotal - n
    print(borrow)
