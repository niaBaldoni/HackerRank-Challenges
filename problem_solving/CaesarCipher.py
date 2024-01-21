#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    lower = ""
    for i in range(ord('a'), ord('z')+1):
        lower += chr(i)
    
    upper = ""
    for i in range(ord('A'), ord('Z')+1):
        upper += chr(i)
        
    out = ""
    for letter in s:
        if letter in lower:
            i = lower.index(letter)
            out += lower[(i+k)%26]
        elif letter in upper:
            i = upper.index(letter)
            out += upper[(i+k)%26]
        else:
            out += letter
    
    return out
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
