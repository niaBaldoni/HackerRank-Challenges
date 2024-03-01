'''
k = int(input())
lista = list(map(int, input().split()))

counts = dict()
for el in lista:
    if el not in counts:
        counts[el] = 1
    else:
        counts[el] += 1

x = min(counts, key=counts.get)

print(x)
'''

k = int(input())
lista = list(map(int, input().split()))

setA, setB = set(), set()
for i in lista:
    if i not in setA:
        setA.add(i)
    else:
        setB.add(i)

print(*setA.difference(setB))
