#!/bin/python3

import math
import os
import random
import re
import sys
"""
Need to complete test cases for very large numbers - goes into runtime error
"""
#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def checkSuperDigit(val):
    add = 0
    for digit in val:
        add = add + int(digit)
        
    if(len(str(add)) == 1):
       return add
    
    else:
        val = str(add)
        return checkSuperDigit(val)
        
def superDigit(n, k):
    # Write your code here
    concatVal = n * k
    return checkSuperDigit(concatVal)
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
