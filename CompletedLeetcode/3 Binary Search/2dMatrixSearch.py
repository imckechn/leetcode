from typing import List


class Solution:
    def findRow(matrix, target):
        if len(matrix) == 1:
            return 0
        
        for i in range(1, len(matrix)):
            if matrix[i][0] > target:
                return i-1
            
        return len(matrix)-1

    def findColumn(matrix, target, y):
        for i in range(len(matrix[y])):
            if matrix[y][i] == target:
                return i
            
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y = Solution.findRow(matrix, target)        
        x = Solution.findColumn(matrix, target, y)
        if x == -1:
            return False
        
        return True

print(Solution.searchMatrix(None, [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))

no = [  [1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]]