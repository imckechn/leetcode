from typing import List


class Solution:
    def search(self, grid, x, y, found):
        next = []

        while x != None:
            grid[x][y] = "2"
            found.add((x,y))

            #Check up
            if y-1 >= 0 and (x, y-1) not in found and grid[x][y-1] == '1':
                next.append((x, y-1))

            #Check down
            if y+1 < len(grid[x]) and (x, y+1) not in found and grid[x][y+1] == '1':
                next.append((x, y+1))

            #Check left
            if x-1 >= 0 and (x-1, y) not in found and grid[x-1][y] == '1':
                next.append((x-1, y))

            #check right
            if x+1 < len(grid) and (x+1, y) not in found and grid[x+1][y] == '1':
                next.append((x+1, y))

            if len(next) != 0:
                x, y = next.pop()
            else:
                x = None

        return grid, found
            

    def numIslands(self, grid: List[List[str]]) -> int:
        found = set()
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i,j) not in found:
                    count += 1
                    grid, found = self.search(grid, i, j, found)

        return count
    

sol = Solution()
sol.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])