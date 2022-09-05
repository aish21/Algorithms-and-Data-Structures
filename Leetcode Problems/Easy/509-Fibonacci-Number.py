'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
'''

class Solution:
    def fib(self, n: int) -> int:
        output = [0 for x in range(n + 1)]
        output[0] = 0
        if(n >= 1):
            output[1] = 1
            for x in range(2, n+1):
                output[x] = output[x - 1] + output[x - 2]
        return output[-1]
        