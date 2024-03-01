setA = set(map(int, input().split()))

check = True

for i in range(int(input())):

    setB = set(map(int, input().split()))

    if not (setA.difference(setB) and not setB.difference(setA)):

        check = False

print(check)
