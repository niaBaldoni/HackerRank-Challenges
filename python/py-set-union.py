n = int(input())
raw_1 = set(input().split(" "))

b = int(input())
raw_2 = set(input().split(" "))

print(len(raw_1.union(raw_2)))
