import math
import os
import random
import re
import sys
"""
Python program to count number of ways
to express X as sum of N-th power
of unique natural numbers.
"""
#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#
c = 0

def count(X, N, num):
    currentValue = (X - pow(num, N))
    if currentValue == 0:
        return c + 1
    if currentValue < 0:
        return 0
    
    return count(currentValue, N, num + 1) + count(X, N, num + 1)

def powerSum(X, N):
    # Write your code here
    return count(X, N, 1)
    

if __name__ == '__main__':
    X = int(input().strip())
    N = int(input().strip())
    result = powerSum(X, N)
    print(result)

