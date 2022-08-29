'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        1. Loop till n
        2. Convert to binary
        3. extract the value
        4. Count number of 1s
        '''
        output = []
        temp = []
        
        for i in range(n + 1):
            x = str(bin(i))
            x = x[2:len(x)]
            temp.append(x)
        
        for i in range(len(temp)):
            y = 0
            for j in range(len(temp[i])):
                if temp[i][j] == '1':
                    y += 1
            output.append(y)
        
        return output
            
        