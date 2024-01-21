from collections import Counter

# first line contains x, the number of shoes
x = int(input())

# second line contains a list of all the shoe sizes in the shop, separated by a space
# we are using the Counter dict subclass to store elements (shoe size) as dictionary keys, and their counts as dictionary values
available_sizes = Counter(map(int, input().split()))

# number of customers
n = int(input())

total = 0

for i in range(n):
    size, price = list(map(int, input().split()))
    if available_sizes[size] > 0:
        total += price
        available_sizes[size] -= 1
print(total)
