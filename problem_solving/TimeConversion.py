import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def convert(arr):
    new = ""
    for letter in arr:
        new += letter
    return new

def timeConversion(s):
    output = list(s)
    
    if output[8] == "P":
        if output[0] != "1" or output[1] != "2":
            output[0] = str(1 + int(s[0]))
            output[1] = str(2 + int(s[1]))
            
    if output[8] == "A":
        if output[0] == "1" and output[1] == "2":
            output[0] = "0"
            output[1] = "0"
    
    output = output[0:8]
    return(convert(output))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
