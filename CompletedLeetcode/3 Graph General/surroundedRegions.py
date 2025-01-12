from typing import List


class Solution:
    def seachAndDestroy(board, x, y):
        peakX = len(board)
        peakY = len(board[0])

        board[x][y] = "Z"
        
        if y+1 < peakY and board[x][y+1] == "O":
            Solution.seachAndDestroy(board, x, y+1)
        if y-1 >= 0 and board[x][y-1] == "O":
            Solution.seachAndDestroy(board, x, y-1)

        if x+1 < peakX and board[x+1][y] == "O":
            Solution.seachAndDestroy(board, x+1, y)
        if x-1 >= 0 and board[x-1][y] == "O":
            Solution.seachAndDestroy(board, x-1, y)

    def solve(self, board: List[List[str]]) -> None:
        peakX = len(board)
        peakY = len(board[0])

        #Visit top
        for i in range(len(board[0])):
            if board[0][i] == "O":
                Solution.seachAndDestroy(board, 0, i)
        #Visit bot
        for i in range(len(board[0])):
            if board[peakX-1][i] == "O":
                Solution.seachAndDestroy(board, peakX-1, i)

        #visit left
        for i in range(len(board)):
            if board[i][0] == "O":
                Solution.seachAndDestroy(board, i, 0)

        #Visit right
        for i in range(len(board)):
            if board[i][peakY-1] == "O":
                Solution.seachAndDestroy(board, i, peakY-1)

        for i in range(peakX):
            for j in range(peakY):
                if board[i][j] ==  "O":
                    board[i][j] = "X"
                elif board[i][j] ==  "Z":
                    board[i][j] = "O"

        return board
        """
        Do not return anything, modify board in-place instead.
        """
        
# Solution.solve(None, [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
# Solution.solve(None, [["X"]])
# Solution.solve(None, [["O","O"],["O","O"]])

Solution.solve(
    None, 
    [["X","O","X"],
    ["O","X","O"],
    ["X","O","X"]]
)