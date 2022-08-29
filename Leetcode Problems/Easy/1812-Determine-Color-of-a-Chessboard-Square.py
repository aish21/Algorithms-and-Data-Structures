'''
You are given coordinates, a string that represents the coordinates of a square of the chessboard.
Return true if the square is white, and false if the square is black.
The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.
'''

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        '''
        - Black: Odd numbers for a,c,e,g; Even numbers for b,d,f,h - FALSE
        - Else TRUE
        '''
        l1 = ['a', 'c', 'e', 'g']
        l2 = ['b', 'd', 'f', 'h']
        
        if(coordinates[0] in l1):
            if(int(coordinates[1]) % 2 == 0):
                return True
            else:
                return False
        else:
            if(int(coordinates[1]) % 2 == 0):
                return False
            else:
                return True
        