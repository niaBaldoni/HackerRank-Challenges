m = int(input())
set1 = set(map(int, input().split()))

n = int(input())
set2 = set(map(int, input().split()))

print(len(set1.symmetric_difference(set2)))
