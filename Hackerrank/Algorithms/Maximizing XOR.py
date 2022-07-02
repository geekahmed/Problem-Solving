#!/bin/python3

import math
import os
import random
import re
import sys
from operator import ixor
from functools import reduce

#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def maximizingXor(l, r):
    # Write your code here
    list1 = [x for x in range(l, r+1)]
    list2 = [x for x in range(l, r+1)]
    
    return max([reduce(ixor,[x,y]) for x in list1 for y in list2])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
