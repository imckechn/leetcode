from cmath import inf
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = []
        updateMade = False

        #Check if up is valid
        if entrance[0] > 0 and maze[entrance[0]-1][entrance[1]] != "+":
            if maze[entrance[0]-1] == 0:
                return 1
            else:
                updateMade = True
                queue.append([entrance[0]-1, entrance[1], 1])
        
        #Check if down is valid
        if entrance[0]+1 < len(maze) and maze[entrance[0]+1][entrance[1]] != "+":
            if maze[entrance[0]+1] == len(maze)-1:
                return 1
            else:
                updateMade = True
                queue.append([entrance[0]+1,entrance[1], 1])
        
        #Check if left is valid
        if entrance[1] > 0 and maze[entrance[0]][entrance[1]-1] != "+":
            if maze[entrance[0]][entrance[1]-1] == 0:
                return 1
            else:
                updateMade = True
                queue.append([entrance[0],entrance[1]-1, 1])

        #Check if right is valid
        if entrance[1]+1 < len(maze[0]) and maze[entrance[0]][entrance[1]+1] != "+":
            if maze[entrance[0]][entrance[1]+1] == len(maze[entrance[0]]):
                return 1
            else:
                updateMade = True
                queue.append([entrance[0],entrance[1]+1, 1])

        if not updateMade:
            return -1

        maze[entrance[0]][entrance[1]] = "+"
        ans = self.bfs(maze, queue)
        if ans == -1:
            return ans
        return ans


    def bfs(self, maze, queue):
        if queue == []:
            return -1

        next = queue.pop(0)

        #check if next is on the edge
        if next[0] == 0 or next[0] == len(maze)-1 or next[1] == 0 or next[1] == len(maze[0])-1:
            return next[2]

        #Check if up is valid
        if next[0] > 0 and maze[next[0]-1][next[1]] != "+":
            if maze[next[0]-1] == 0:
                return 1
            else:
                queue.append([next[0]-1,next[1], next[2]+1])
        
        #Check if down is valid
        if next[0]+1 < len(maze) and maze[next[0]+1][next[1]] != "+":
            if maze[next[0]+1] == len(maze)-1:
                return 1
            else:
                queue.append([next[0]+1,next[1], next[2]+1])
        
        #Check if left is valid
        if next[1] > 0 and maze[next[0]][next[1]-1] != "+":
            if maze[next[0]][next[1]-1] == 0:
                return 1
            else:
                queue.append([next[0],next[1]-1, next[2]+1])

        #Check if right is valid
        if next[1]+1 < len(maze[0]) and maze[next[0]][next[1]+1] != "+":
            if maze[next[0]][next[1]+1] == len(maze[next[0]]):
                return 1
            else:
                queue.append([next[0],next[1]+1, next[2]+1])

        maze[next[0]][next[1]] = "+"

        return self.bfs(maze, queue)


sol = Solution()

#Test 1
maze = [["+","+",".","+"],
        [".",".",".","+"],
        ["+","+","+","."]]

entrance = [1,2]
expected = 1
answer = sol.nearestExit(maze, entrance)

if answer != expected:
    print("Test 1 failed")
else:
    print("Test 1 passed")

#Test 2
maze = [["+","+","+"],
        [".",".","."],
        ["+","+","+"]]

entrance = [1,0]
expected = 2
answer = sol.nearestExit(maze, entrance)

if answer != expected:
    print("Test 2 failed")
else:
    print("Test 2 passed")

#Test 3
maze = [[".","+"]]

entrance = [0,0]
expected = -1
answer = sol.nearestExit(maze, entrance)

if answer != expected:
    print("Test 3 failed")
else:
    print("Test 3 passed")


#Test 4
maze = [["+",".","+","+","+","+","+"],
 ["+",".","+",".",".",".","+"],
 ["+",".","+",".","+",".","+"],
 ["+",".",".",".","+",".","+"],
 ["+","+","+","+","+",".","+"]]

entrance = [0,1]
expected = 12
answer = sol.nearestExit(maze, entrance)

if answer != expected:
    print("Test 4 failed")
else:
    print("Test 4 passed")

#Test 5
maze = [["+",".","+","+","+","+","+"],
        ["+",".","+",".",".",".","+"],
        ["+",".","+",".","+",".","+"],
        ["+",".",".",".",".",".","+"],
        ["+","+","+","+",".","+","."]]

entrance = [0,1]
expected = 7
answer = sol.nearestExit(maze, entrance)

if answer != expected:
    print("Test 4 failed")
else:
    print("Test 4 passed")


