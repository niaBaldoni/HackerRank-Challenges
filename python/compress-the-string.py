from itertools import groupby

L = input()

"""
ris = ""
lista = []
for key, group in groupby(L):
    ris += f"({len(list(group))}, {key}) "
print(ris)

"""

out = [(len(list(group)), int(key)) for key, group in groupby(L)]
print(*out, sep=" ")
