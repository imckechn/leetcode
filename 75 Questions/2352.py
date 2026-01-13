from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        found = {}
        total = 0

        for row in grid:
            row = tuple(row)
            if row in found:
                found[row] += 1
            else:
                found[row] = 1

        res = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

        for row in res:
            row = tuple(row)
            if row in found:
                total += found[row]

        return total
        


sol = Solution()

print(sol.equalPairs([[3,2,1],
                      [1,7,6],
                      [2,7,7]]))

print(sol.equalPairs([[3,1,2,2],
                      [1,4,4,5],
                      [2,4,2,2],
                      [2,4,2,2]]))
