from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        return self.findNearest(maze, entrance, [entrance])
    
    def findNearest(self, maze, current, visited):
        # (height, width)

        #Check if it's at an exit
        if current not in visited and (current[0] == 0 or current[0] == len(current) -1 or current[1] == 0 or current[1] == len(current) -1):
            return 1

        #Check if up is valid
        if current[0] > 0 and maze[current[0]-1][current[1]] != "+" and  [current[0]-1, current[1]] not in visited:
            visited.append([current[0], current[1]])
            current[0] = current[0]-1
        
        #Check if down is valid
        if current[0]+1 < len(maze[1])-1 and maze[current[0]+1][current[1]] != "+" and  [current[0]+1, current[1]] not in visited:
            visited.append([current[0], current[1]])
            current[0] = current[0]+1
        
        #Check if left is valid
        if current[1] > 0 and maze[current[0]][current[1]-1] != "+" and  [current[0], current[1]-1] not in visited:
            visited.append([current[0], current[1]])
            current[1] = current[1]-1

        #Check if right is valid
        if current[1]+1 < len(maze[1])-1 and maze[current[0]][current[1]+1] != "+" and  [current[1], current[1]+1] not in visited:
            visited.append([current[0], current[1]])
            current[1] = current[1]+1

        return 1 + self.findNearest(maze, current, visited)
        

sol = Solution()

#Test 1
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
# sol = Solution()

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