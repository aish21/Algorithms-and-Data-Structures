'''
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
'''

class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if(len(mat) == 0 or len(mat[0]) == 0):
            return []
        
        column = len(mat)
        row = len(mat[0])
        numbers = row * column 
        output = []
        m = 0
        n = 0
        flag = True
        
        for i in range(numbers):
            output.append(mat[m][n])
            
            if flag:
                m-=1
                n+=1
                
            else:
                m+=1
                n-=1
                
            if m >= column:
                m-=1
                n+=2
                flag=True
                
            elif n >= row:
                m+=2
                n-=1
                flag=False
                
            if m<0:
                m=0
                flag=False
                
            elif n<0:
                n=0
                flag=True
        
        return output