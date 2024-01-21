from collections import defaultdict

n, m = input().split()
a = defaultdict(list)
lista = []

for i in range(int(n)):
    temp = input()
    lista.append(temp)
    a[temp].append(len(lista))

for i in range(int(m)):
    temp = input()
    if temp in a:
        print(*a[temp])
    else:
        print(-1)
