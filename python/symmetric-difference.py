
m = int(input())
listaM = list(map(int, input().split()))

n = int(input())
listaN = list(map(int, input().split()))

print("\n".join(map(str, sorted([x for x in set(listaM).union(set(listaN)) - set(listaM).intersection(set(listaN))]))))
