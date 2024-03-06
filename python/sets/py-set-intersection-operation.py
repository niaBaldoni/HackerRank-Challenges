n = int(input())
setN = set(map(int, input().split()))

b = int(input())
setB = set(map(int, input().split()))

print(len(setN.intersection(setB)))
