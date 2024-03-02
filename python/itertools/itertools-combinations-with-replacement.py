from itertools import combinations_with_replacement

s, k = input().split()
 
out = ["".join(i) for i in combinations_with_replacement(sorted(s), int(k))]

print(*out, sep="\n")
