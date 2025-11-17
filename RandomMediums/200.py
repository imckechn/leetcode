from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    if (j > 0 and grid[i][j-1] == "1") and (i > 1 and grid[i-1][j] == "1") and grid[i-1][j-1] == "0":
                        count -= 1

                    elif (j == 0 or grid[i][j-1] == "0") and (i == 0 or grid[i-1][j] == "0"):
                        count += 1
        
        return count
                    #If to the left and above are counted, minus one

                    #elif only to the left or only above are counted, don't increase count

                    # else increase count

sol = Solution()
print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))