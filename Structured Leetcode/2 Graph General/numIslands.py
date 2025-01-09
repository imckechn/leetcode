from typing import List, Optional

class Solution:
    def search(grid, i, j):
        grid[i][j] = "0"

        if i + 1 < len(grid):
            if grid[i+1][j] == "1":
                Solution.search(grid, i+1, j)

        if j + 1 < len(grid[0]):
            if grid[i][j+1] == "1":
                Solution.search(grid, i, j+1)

        if i - 1 >= 0:
            if grid[i-1][j] == "1":
                Solution.search(grid, i-1, j)

        if j - 1 >= 0:
            if grid[i][j-1] == "1":
                Solution.search(grid, i, j-1)

    def numIslands(grid: List[List[str]]) -> int:
        islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    Solution.search(grid, i, j)

        return islands


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"]
]

# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]

# grid = [
#     ["1","1","1","1"],
#     ["0","0","0","1"],
#     ["1","1","1","1"]
# ]

# grid = [
#     ["1","1","1"],
#     ["0","1","0"],
#     ["1","1","1"]
# ]

print(Solution.numIslands(grid))