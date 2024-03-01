#the code in quotes is how you would solve it manually
"""
word, k = input().split(" ")
k = int(k)
s_list = []
for lett in parola:
    s_list.append(lett)
s_list.sort()

out_list = list(permutations(s_list, k))

ris = ""
for i in out_list:
    for a in i:
        ris += a
    ris += "\n"
print(ris)
"""
#but if you're doing it manually, then why are you using Python?


word, k = input().split(" ")

out_list = ["".join(i) for i in list(permutations(sorted(word), int(k)))]
print(*out_list, sep="\n")
