#https://www.hackerrank.com/challenges/counting-valleys/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    mountain = valley = 0
    for word in path:
        mountain += 1 if word == 'U' else -1
        valley += 1 if mountain == 0 and word == 'U' else 0
    return valley
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
