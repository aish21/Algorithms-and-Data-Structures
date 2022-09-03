'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if(n <= 2): 
            return n
        
        output = [0]*(n+1)
        output[1] = 1
        output[2] = 2
        for i in range(3,n+1):
            output[i] = output[i-1] + output[i-2]
        return output[n]