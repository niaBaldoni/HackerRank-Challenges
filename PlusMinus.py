import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pcounter = 0
    mcounter = 0
    zcounter = 0
    for i in range(0, len(arr)):
        if arr[i] < 0:
            minusc += 1
        if arr[i] == 0:
            zeroc += 1
        if arr[i] > 0:
            plusc += 1
    
    print(float("{:.6f}".format(pcounter/len(arr))))
    print(float("{:.6f}".format(mcounter/len(arr))))
    print(float("{:.6f}".format(zcounter/len(arr))))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
