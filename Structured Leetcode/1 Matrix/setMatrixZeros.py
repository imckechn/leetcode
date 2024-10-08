class Solution:
    def setRow(matrix, row):
        for i in range(len(matrix[row])):
            if matrix[row][i] != 0:
                matrix[row][i] = None
        
        return matrix
    
    def setColumn(matrix, column):
        for i in range(len(matrix)):
            if matrix[i][column] != 0:
                matrix[i][column] = None
        
        return matrix


    def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        columns = []

        lenx = len(matrix)
        leny = len(matrix[0])

        for row in range(lenx):
            for column in range(leny):
                if matrix[row][column] == 0:
                    rows.append(row)
                    columns.append(column)

        for row in range(lenx):
            if row in rows:
                matrix[row] = [0] * leny
            else:
                for col in columns:
                    matrix[row][col] = 0

        print(matrix)

        
Solution.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
Solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])