from typing import List

class Solution:
    def ufs(tri, row, mem): #Need to try bottom up
        newRow = []

        for i in range(len(tri[row])):
            if tri[row][i] + mem[i] < tri[row][i] + mem[i+1]:
                newRow.append(tri[row][i] + mem[i])
            else:
                newRow.append(tri[row][i] + mem[i+1])

        if len(newRow) == 1:
            return newRow[0]

        return Solution.ufs(tri, row-1, newRow)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        ans = Solution.ufs(triangle, len(triangle)-2, triangle[-1])
        return ans

print(Solution.minimumTotal(None, [[2],[3,4],[6,5,7],[4,1,8,3]])) #11
print(Solution.minimumTotal(None, [[-10]])) #-10
print(Solution.minimumTotal(None, [[1],[-5,-2],[3,6,1],[-1,2,4,-3]])) #-3

# [[1],
#  [-5,-2],
#  [3,6,1],
#  [-1,2,4,-3]]