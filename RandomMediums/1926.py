from cmath import inf
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        return self.findNearest(maze, entrance, [entrance[:]])
    
    def findNearest(self, maze, current, visited):
        #Check if it's at an exit
        if current not in visited and (current[0] == 0 or current[0] == len(maze) -1 or current[1] == 0 or current[1] == len(maze[0]) -1):
            return 0
        
        ans1, ans2, ans3, ans4 = float(inf), float(inf), float(inf), float(inf)
        visited.append(current[:])
        new = current

        #Check if up is valid
        if current[0] > 0 and maze[current[0]-1][current[1]] != "+" and  [current[0]-1, current[1]] not in visited:
            new[0] = current[0]-1
            ans1 = self.findNearest(maze, current, visited)
            ans1 = ans1 if ans1 != -1 else float(inf)
        
        #Check if down is valid
        if current[0]+1 < len(maze) and maze[current[0]+1][current[1]] != "+" and  [current[0]+1, current[1]] not in visited:
            new[0] = current[0]+1
            ans2 = self.findNearest(maze, current, visited)
            ans2 = ans2 if ans2 != -1 else float(inf)
        
        #Check if left is valid
        if current[1] > 0 and maze[current[0]][current[1]-1] != "+" and  [current[0], current[1]-1] not in visited:
            new[1] = current[1]-1
            ans3 = self.findNearest(maze, current, visited)
            ans3 = ans3 if ans3 != -1 else float(inf)

        #Check if right is valid
        if current[1]+1 < len(maze[0]) and maze[current[0]][current[1]+1] != "+" and  [current[1], current[1]+1] not in visited:
            new[1] = current[1]+1
            ans4 = self.findNearest(maze, current, visited)
            ans4 = ans4 if ans4 != -1 else float(inf)

        if min( min(ans1, ans2), min(ans3,ans4)) == float(inf):
            return -1
 
        return 1 + min( min(ans1, ans2), min(ans3,ans4))
        

sol = Solution()

# #Test 1
# maze = [["+","+",".","+"],
#         [".",".",".","+"],
#         ["+","+","+","."]]

# entrance = [1,2]
# expected = 1
# answer = sol.nearestExit(maze, entrance)

# if answer != expected:
#     print("Test 1 failed")
# else:
#     print("Test 1 passed")

# #Test 2
# maze = [["+","+","+"],
#         [".",".","."],
#         ["+","+","+"]]

# entrance = [1,0]
# expected = 2
# answer = sol.nearestExit(maze, entrance)

# if answer != expected:
#     print("Test 2 failed")
# else:
#     print("Test 2 passed")

# #Test 3
# maze = [[".","+"]]

# entrance = [0,0]
# expected = -1
# answer = sol.nearestExit(maze, entrance)

# if answer != expected:
#     print("Test 3 failed")
# else:
#     print("Test 3 passed")


# #Test 4
# maze = [["+",".","+","+","+","+","+"],
#  ["+",".","+",".",".",".","+"],
#  ["+",".","+",".","+",".","+"],
#  ["+",".",".",".","+",".","+"],
#  ["+","+","+","+","+",".","+"]]

# entrance = [0,1]
# expected = 12
# answer = sol.nearestExit(maze, entrance)

# if answer != expected:
#     print("Test 4 failed")
# else:
#     print("Test 4 passed")

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


