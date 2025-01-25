from typing import List


class Solution:
    def findRow(matrix, target):
        if len(matrix) == 1:
            return 0
        
        for i in range(1, len(matrix)):
            if matrix[i][0] > target:
                return i-1
            
        return False

    def findColumn(matrix, target, y):
        for i in range(len(matrix[y])):
            if matrix[y][i] == target:
                return i
            
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y = Solution.findRow(matrix, target)

        if not y:
            return False
        
        x = Solution.findColumn(matrix, target, y)
        if not x:
            return False
        
        return True

