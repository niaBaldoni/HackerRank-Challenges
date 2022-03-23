# I have commented out the three incorrect lines
# First error is when we calculate the middle of the array
# If we have 5 elements -> n = 5, mid = 3
# however, arrays start at 0, so the middle element is actually at a[2]

# Second error is when we declare the start and end of the part of the array we want to flip
# We already flipped a[mid] with a[n-1], so we need to flip a[mid+1] with a[n-2]

# Third error is in the while loop
# st needs to increase, but ed needs to decrease


def findZigZagSequence(a, n):
    a.sort()
    #mid = int((n + 1)/2)
    mid = int((n + 1)/2) - 1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    #ed = n - 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        #ed = ed + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
