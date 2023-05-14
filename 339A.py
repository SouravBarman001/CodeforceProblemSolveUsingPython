

k = input()
l = len(k) + 1
L = []
for i in range(1, l):
    if i % 2 == 1:
        L.append(k[i - 1])

L = sorted(L)
le = len(L)
K = []
for i in range(0, le):
    K.append(L[i])
    K.append('+')

print(''.join(K[:-1]))
