'''
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
'''

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = [[0 for i in range(0, len(matrix))] for j in range(0, len(matrix[0]))]
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                output[j][i] = matrix[i][j]
        
        return output
        