n, m = input().split()
arr = [int(x) for x in input().split()]
A = set([int(x) for x in input().split()])
B = set([int(x) for x in input().split()])

print(sum([(i in A) - (i in B) for i in arr]))
