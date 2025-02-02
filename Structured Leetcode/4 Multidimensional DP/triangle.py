from typing import List

class Solution:
    def dfs(tri, x, y): #Need to try bottom up
        if x == len(tri):
            return 0
        
        if x+1 < len(tri):
            if tri[x+1][y+1] == "None":
                return tri[x][y] + tri[x+1][y]
            elif  tri[x+1][y] == "None":
                return tri[x][y] + tri[x+1][y+1]

        a = Solution.dfs(tri, x+1, y)
        b = Solution.dfs(tri, x+1, y+1)

        if a<b:
            if x+1 < len(tri):
                tri[x+1][y+1] = "None"
                tri[x+1][y] = a
            return tri[x][y] + a
        
        if x+1 < len(tri):
            tri[x+1][y] = "None"
            tri[x+1][y+1] = b
        return tri[x][y] + b

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = Solution.dfs(triangle, 0, 0)
        return ans

# print(Solution.minimumTotal(None, [[2],[3,4],[6,5,7],[4,1,8,3]]))
# print(Solution.minimumTotal(None, [[-10]]))
print(Solution.minimumTotal(None, [[1],[-5,-2],[3,6,1],[-1,2,4,-3]])) #-3

# [[1],
#  [-5,-2],
#  [3,6,1],
#  [-1,2,4,-3]]