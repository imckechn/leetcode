from typing import List, Optional

class Solution:
    def numIslands(grid: List[List[str]]) -> int:
        islands = 0
        streak = False

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islands += 1

                    if i > 0 and grid[i-1][j] == "1":
                        islands -= 1
                    
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