from itertools import combinations
"""
s, k = input().split()

out = []
for i in range(1, int(k)+1):
    temp = list(combinations(sorted(s), i))
    for el in temp:
        out.append(el)
out_list = ["".join(i) for i in out]

print(*out_list, sep="\n")

"""

s, k = input().split()

out_list = ["".join(i) for j in range(1, int(k)+1) for i in combinations(sorted(s), j)]

print(*out_list, sep="\n")
