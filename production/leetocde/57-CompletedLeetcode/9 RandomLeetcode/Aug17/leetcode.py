class Solution:
    def isValidSudoku(board):

        for i in range(9):
            foundChars = []
            for j in range(9):
                if board[i][j] != ".":
                    if len(foundChars) > 0 and board[i][j]in foundChars:
                        return False
                    else:
                        foundChars.append(board[i][j])

        for i in range(9):
            foundChars = []
            for j in range(9):
                if board[j][i] != ".":
                    if len(foundChars) > 0 and board[j][i]in foundChars:
                        return False
                    else:
                        foundChars.append(board[j][i])


        #Loop through first three rows, if the first three chars have the same val, fail else
        for a in range(0, 7, 3):# for the three top rows
            for b in range(0, 7, 3):# for the three top rows
                foundChars = []
                for i in range(3):
                    for j in range(3):
                        elem = board[i+a][j+b]
                        if board[i+a][j+b] != ".":
                            if board[i+a][j+b] in foundChars:
                                return False
                            else:
                                foundChars.append(board[i+a][j+b])

        return True
    

# 0+0

# 0+1

#
    
if Solution.isValidSudoku(  #False
     [[".","4",".", "3",".",".", ".",".","."],
      [".",".",".", ".",".","3", ".",".","1"],
      ["8",".",".", ".",".",".", ".","2","."],
     
      [".",".","2", ".","7",".", ".",".","."],
      [".","1","5", ".",".",".", ".",".","."],
      [".",".",".", ".","5",".", ".","1","."],

      [".",".",".", ".",".","2", ".",".","."],
      [".","2",".", "9",".",".", ".",".","."],
      [".",".","4", ".",".",".", ".",".","."]]
) == True:
    print("True")
else:
    print("False")
    
if Solution.isValidSudoku(  #True
     [["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]]
) == True:
    print("True")
else:
    print("False")