from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        turns = 0
        
        #Find all rotten oranges
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i,j])

        directions = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1]
        ]

        #Turn da oranges rotten
        while queue != []:
            turns += 1
            newQueue = []

            for i in range(len(queue)):
                x, y = queue.pop()

                for dir in directions:
                    newX = x + dir[0]
                    newY = y + dir[1]

                    if newX >= len(grid) or newY >= len(grid[newX]) or newX < 0 or newY < 0:
                        continue

                    if grid[newX][newY] == 1:
                        grid[newX][newY] = 2
                        newQueue.append([newX, newY])
                        
            if newQueue == []:
                turns -= 1

            queue = newQueue

        #See if there's a fresh orange
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return turns
    

sol = Solution()

#Test 1
input = [[2,1,1],[1,1,0],[0,1,1]]
expected = 4
ans = sol.orangesRotting(input)

if ans == expected:
    print("Test 1 passed")
else:
    print("Test 1 failed")


#Test 2
input = [[2,1,1],[0,1,1],[1,0,1]]
expected = -1
ans = sol.orangesRotting(input)

if ans == expected:
    print("Test 2 passed")
else:
    print("Test 2 failed")
    print("Test 1 failed")


#Test 3
input = [[0,2]]
expected = 0
ans = sol.orangesRotting(input)

if ans == expected:
    print("Test 2 passed")
else:
    print("Test 2 failed")