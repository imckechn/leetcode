from typing import List

class Types:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
    
    def getCoordinates(self):
        return [self.x, self.y]
    
    def getType(self):
        return self.type


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        count = 0
        counts = []
        grid = [ [0]*n for _ in range(m) ]
        takenTypes = [0]

        for position in positions:
            if grid[position[0]][position[1]] != 0:
                counts.append(count)
                continue

            sideTypes = self.getSideTypes(grid, m, n, position)

            if len(sideTypes) == 0:
                takenTypes.append(takenTypes[-1] + 1)
                grid[position[0]][position[1]] =takenTypes[-1]
                count += 1

            elif len(sideTypes) == 1:
                grid[position[0]][position[1]] = sideTypes[0].getType()

            else:
                #Need to init the new island
                grid, baseType, count = self.removeIslands(grid, m, n, sideTypes, count)
                grid[position[0]][position[1]] = baseType

                #Update the grid with the type
            
            counts.append(count)
        return counts
    

    def getSideTypes(self, grid, m, n, position):
        types = []

        #Check up
        if position[0] >= 1 and grid[position[0]-1][position[1]] != 0:
            types.append(Types(position[0]-1, position[1], grid[position[0]-1][position[1]]))

        #Check down
        if position[0] < m-1 and grid[position[0]+1][position[1]] != 0:
            types.append(Types(position[0]+1, position[1], grid[position[0]+1][position[1]]))

        #Check left
        if position[1] >= 1 and grid[position[0]][position[1]-1] != 0:
            types.append(Types(position[0], position[1]-1, grid[position[0]][position[1]-1]))

        #Check right
        if position[1] < n-1 and grid[position[0]][position[1]+1] != 0:
            types.append(Types(position[0], position[1]+1, grid[position[0]][position[1]+1]))

        return types

    def removeIslands(self, grid, m, n, sideTypes, count):
        baseType = sideTypes.pop().getType()
        seen = [baseType]

        for type in sideTypes:
            typeOfType = type.getType()
            if typeOfType != baseType:
                if typeOfType not in seen:
                    seen.append(typeOfType)
                    count -= 1
                grid = self.bfs(grid, m, n, type.getCoordinates(), baseType)

        return grid, baseType, count
    
    def bfs(self, grid, m, n, coord, baseType):
        queue = [coord]

        while len(queue) != 0:
            elem = queue.pop()

            grid[elem[0]][elem[1]] = baseType

            #Check up
            if elem[0] >= 1 and grid[elem[0]-1][elem[1]] != baseType and grid[elem[0]-1][elem[1]] != 0:
                queue.append([elem[0]-1, elem[1]])

            #Check down
            if elem[0] < m-1 and grid[elem[0]+1][elem[1]] != baseType and grid[elem[0]+1][elem[1]] != 0:
                queue.append([elem[0]+1, elem[1]])

            #Check left
            if elem[1] >= 1 and grid[elem[0]][elem[1]-1] != baseType and grid[elem[0]][elem[1]-1] != 0:
                queue.append([elem[0], elem[1]-1])

            #Check right
            if elem[1] < n-1 and grid[elem[0]][elem[1]+1] != baseType and grid[elem[0]][elem[1]+1] != 0:
                queue.append([elem[0], elem[1]+1])

        return grid




sol = Solution()

expected = [1,1,2,3,3,3,2,2,1,1]
ans = sol.numIslands2(3, 3, [[0,0],[0,1],[1,2],[2,1],[1,0],[0,0],[2,2],[1,2],[1,1],[0,1]])
if ans != expected:
    print("Failed, got " + str(ans))
else:
    print("Passed")