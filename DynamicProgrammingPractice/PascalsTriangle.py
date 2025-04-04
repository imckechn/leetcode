from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        prevRows = Solution.generate(self, numRows-1)

        currRow = [1]

        for i in range(1, len(prevRows[-1])):
            currRow.append(prevRows[-1][i-1] + prevRows[-1][i])

        currRow.append(1)
        prevRows.append(currRow)

        return prevRows
    

print(Solution.generate(None, 5))
print(Solution.generate(None, 1))