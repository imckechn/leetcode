from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        toRot = set()

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 2:
                    toRot.add((x,y))

        count = 1
        while len(toRot) != 0:
            nextRound = set()

            for x,y in toRot:
    
                #Check top
                if y-1>=0 and grid[x][y-1] == 1:
                    nextRound.add((x, y-1))
                    grid[x][y-1] = 2

                #Check bottom
                if y+1<len(grid[x]) and grid[x][y+1] == 1:
                    nextRound.add((x, y+1))
                    grid[x][y+1] = 2

                #Check right
                if x+1 < len(grid) and grid[x+1][y] == 1:
                    nextRound.add((x+1, y))
                    grid[x+1][y] = 2

                #Check left
                if x-1 >= 0 and grid[x-1][y] == 1:
                    nextRound.add((x-1, y))
                    grid[x-1][y] = 2

            toRot = nextRound
            count += 1

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    return -1

        return count-1
    
sol = Solution()

print(sol.orangesRotting([[0]]))
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))