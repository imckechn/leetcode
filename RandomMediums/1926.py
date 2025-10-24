from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        return self.findNearest(maze, entrance, [entrance])
    
    def findNearest(maze, current, visited):
        #Check if it's at an exit
        if current[]

        #Check if up is valid
        if current[0] > 0 and maze[current[0]-1][current[1]] != "+" and  [current[0]-1, current[1]] not in visited:
            visited.append(current)
            sol.findNearest()
        

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
sol = Solution()

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