from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue = self.findFirstIsland(grid)
        return self.findFirstIslandConnection(grid, queue)-1

    def findFirstIslandConnection(self, grid, queue):
        visited = queue.copy()

        while queue != []:
            elem = queue.pop(0)
            distance = grid[elem[0]][elem[1]]

            if elem not in visited:
                visited.append(elem)

            #Check up
            if elem[0] >= 1 and [elem[0]-1, elem[1]] not in visited:
                if grid[elem[0]-1][elem[1]] == 1:
                    return distance
                elif grid[elem[0]-1][elem[1]] == 0:
                    grid[elem[0]-1][elem[1]] = distance + 1
                    queue.append([elem[0]-1, elem[1]])

            #Check down
            if elem[0] < len(grid)-1 and [elem[0]+1, elem[1]] not in visited:
                if grid[elem[0]+1][elem[1]] == 1:
                    return distance
                elif grid[elem[0]+1][elem[1]] == 0:
                    grid[elem[0]+1][elem[1]] = distance + 1
                    queue.append([elem[0]+1, elem[1]])

            #Check left
            if elem[1] >= 1  and [elem[0], elem[1]-1] not in visited:
                if grid[elem[0]][elem[1]-1] == 1:
                    return distance
                elif grid[elem[0]][elem[1]-1] == 0:
                    grid[elem[0]][elem[1]-1] = distance + 1
                    queue.append([elem[0], elem[1]-1])

            #Check right
            if elem[1] < len(grid[0])-1 and [elem[0], elem[1]+1] not in visited:
                if grid[elem[0]][elem[1]+1] == 1:
                    return distance
                elif grid[elem[0]][elem[1]+1] == 0:
                    grid[elem[0]][elem[1]+1] = distance + 1
                    queue.append([elem[0], elem[1]+1])
        return 0

    def findFirstIsland(self, grid):
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue = [[i, j]]
                    break
            
            if queue != []:
                break

        return queue + self.dfs(grid, queue[0], [])
    
    def dfs(self, grid, coord, visited):
        if coord in visited:
            return []
        else:
            visited.append(coord)
        
        coords = []
        #Check up
        if coord[0] >= 1 and grid[coord[0]-1][coord[1]] == 1:
            coords += self.dfs(grid, [coord[0]-1, coord[1]], visited)

        #Check down
        if coord[0] < len(grid)-1 and grid[coord[0]+1][coord[1]] == 1:
            coords += self.dfs(grid, [coord[0]+1, coord[1]], visited)

        #Check left
        if coord[1] >= 1 and grid[coord[0]][coord[1]-1] == 1:
            coords += self.dfs(grid, [coord[0], coord[1]-1], visited)

        #Check right
        if coord[1] < len(grid[0])-1 and grid[coord[0]][coord[1]+1] == 1:
            coords += self.dfs(grid, [coord[0], coord[1]+1], visited)

        return coords + [coord]


sol = Solution()
grid = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]

print(sol.shortestBridge(grid))


grid = [[0,1,0],
        [0,0,0],
        [0,0,1]]

print(sol.shortestBridge(grid))