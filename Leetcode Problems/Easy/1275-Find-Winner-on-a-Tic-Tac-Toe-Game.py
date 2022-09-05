'''
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

'''

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        winningMoves = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        array = []
        l1 = len(moves)
        l2 = len(winningMoves)
        for i in moves:
            array.append(3*i[0] + i[1])
            A = array[0:l1:2]
            B = array[1:l1:2]
            B.sort()
            A.sort()
        for winningMoves in winningMoves:
            if all([i in A for i in winningMoves]):
                return 'A'
            elif all([i in B for i in winningMoves]):
                return 'B'
        if l1 == 9:
            return "Draw"
        else:
            return "Pending"
        