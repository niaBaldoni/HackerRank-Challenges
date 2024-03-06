
tests = int(input())

for i in range(tests):
    input()
    setA = set(map(int, input().split()))
    input()
    setB = set(map(int, input().split()))

    print(not bool(setA.difference(setB)))
