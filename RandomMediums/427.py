from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]):
        if len(grid) < 2:
            return Node(grid[0][0], True, None, None, None, None)

        return self.constructNode(grid, 0, len(grid[0]), 0, len(grid))

    def constructNode(self, grid, left, right, top, bottom):
        #Base caase
        if right - left == 2:
            #Check for all one number
            if grid[top][left] == grid[top][right-1] and grid[top][left] == grid[bottom-1][left] and grid[top][left] == grid[bottom-1][right-1]:
                if grid[top][left] == 1:
                    return Node(True, True, None, None, None, None)
                else:
                    return Node(False, True, None, None, None, None)
            else:
                 return Node(False, 
                            False, 
                            Node(grid[top][left], True, None, None, None, None),
                            Node(grid[top][right-1], True, None, None, None, None),
                            Node(grid[bottom-1][left], True, None, None, None, None),
                            Node(grid[bottom-1][right-1], True, None, None, None, None)
                        )
            
        else:
            topLeft = self.constructNode(grid, left, left + (right-left)//2, top, top + (bottom-top)//2)
            topRight = self.constructNode(grid,  left + (right-left)//2, right,  top,  top + (bottom-top)//2)
            bottomLeft = self.constructNode(grid, left, left + (right-left)//2,  top + (bottom-top)//2, bottom)
            bottomRight = self.constructNode(grid,  left + (right-left)//2, right,  top + (bottom-top)//2, bottom)

            if (topLeft.isLeaf 
                and topRight.isLeaf 
                and bottomLeft.isLeaf 
                and bottomRight.isLeaf
                and topLeft.val == topRight.val 
                and topLeft.val == bottomLeft.val 
                and topLeft.val == bottomRight.val
            ):
                return Node(topLeft.val, True, None, None, None, None)
            return Node(None, False, topLeft, topRight, bottomLeft, bottomRight)
        
sol = Solution()
grid = [[0,1],[1,0]]
sol.construct(grid)

grid = [[1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0]]
ans = sol.construct(grid)
print(ans)
