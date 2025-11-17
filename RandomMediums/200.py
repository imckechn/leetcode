from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid = self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid, i , j):
        queue = [[i, j]]
        gridHeight = len(grid)
        gridWidth = len(grid[0])

        while len(queue) != 0:
            n, m = queue.pop(0)
                            
            #check above it
            if n > 0 and grid[n-1][m] == "1":
                queue.append([n-1, m])

            #Check bellow it
            if n < gridHeight-1 and grid[n+1][m] == "1":
                queue.append([n+1, m])

            #Check to the left
            if m > 0 and grid[n][m-1] == "1":
                queue.append([n, m-1])

            #Check to the right
            if m < gridWidth-1 and grid[n][m+1] == "1":
                queue.append([n, m+1])

            grid[n][m] = "0"

        return grid


sol = Solution()
print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))