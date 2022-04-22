#!/bin/python3

import math
import os
import random
import re
import sys

#
# Modified Binary Search to find the position of the new score in the leaderboard.
# Instead of just checking array[mid], we also check array[mid - 1] and array[mid + 1]
# This way, we always find the right spot for the new score
#

def binary_search(array, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        
        if array[mid] == x:
            return mid
        
        elif (array[mid] < x) and (array[mid - 1] > x):
            return mid
        
        elif (array[mid] > x) and (array[mid + 1] < x):
            return mid + 1
        
        elif array[mid] < x:
            return binary_search(array, low, mid - 1, x)
    
        else:
            return binary_search(array, mid + 1, high, x)   
    else:
        return -2
    
def climbingLeaderboard(ranked, player):

    # Creating a new ranked list without duplicates
    
    ranked_new = []
    last = -1
    for element in ranked:
        if element != last:
            ranked_new.append(element)
            last = element
    print(ranked_new)
    
    # In the loop, I check if the element is bigger than the top score or smaller than the lowest score
    # If neither, we use the modified Binary Search
    
    ranks = []
    e = len(ranked_new)
    for i in range(len(player)):
        x = player[i]
        if x < ranked_new[e-1]:
            ranks.append(e+1)
        elif x > ranked_new[0]:
            ranks.append(1)
        else:
            index = binary_search(ranked_new, 0, e-1, x) + 1
            ranks.append(index)
        
                
    return ranks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
