from typing import List


class Solution:
    def hasRipe(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return True

        return False

    def findRotten(self, grid, time):
        rotten = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotten.append([[i,j], time])
                
        return rotten

    def turnRotten(self, orange, grid):
        nextRotten = []
        x = orange[0][0]
        y = orange[0][1]
        newTime = orange[1] + 1

        #Orange above
        if x > 0:
            if grid[x-1][y] == 1:
                nextRotten.append([[x-1, y], newTime])
        
        #Orange bellow
        if x < len(grid)-1:
            if grid[x+1][y] == 1:
                nextRotten.append([[x+1, y], newTime])

        #Right Orange
        if y > 0:
            if grid[x][y-1] == 1:
                nextRotten.append([[x, y-1], newTime])

        #Left Orange
        if y < len(grid[x])-1:
            if grid[x][y+1] == 1:
                nextRotten.append([[x, y+1], newTime])

        return nextRotten

    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        queue += self.findRotten(grid, 0)
        currentTime = 0

        while queue:
            orange = queue.pop(0)

            currentTime = orange[1]

            grid[orange[0][0]][orange[0][1]] = 2

            newRotten = self.turnRotten(orange, grid)

            for new in newRotten:
                canBeInseterted = True
                for old in queue:
                    if new[0] == old[0]:
                        canBeInseterted = False
                        break

                if canBeInseterted:
                    queue += [new]

        if self.hasRipe(grid):
            return -1
        return currentTime
    

sol = Solution()
gridA = [[2,1,1],[1,1,0],[0,1,1]]
gridB = [[2,2],
          [1,1],
          [0,0],
          [2,0]]

print(sol.orangesRotting(gridA))
print(sol.orangesRotting(gridB))