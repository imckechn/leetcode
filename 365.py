class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        return self.dfs(x, 0, y, 0, target, [])

    def dfs(self, xVol, xCur, yVol, yCur, target, visited):
        if [xCur, yCur] in visited:
            return False
        elif xCur + yCur == target:
            return True
        else:
            visited.append([xCur, yCur])
            visited.append([xCur, 0])
            visited.append([0, yCur])

        #Adding water to x
        ans = self.dfs(xVol, xVol, yVol, yCur, target, visited)
        if ans:
            return ans

        #Adding water to y
        ans = self.dfs(xVol, xCur, yVol, yVol, target, visited)
        if ans:
            return ans

        #Transfer x to y
        newY = xCur + yCur
        if newY > yVol:
            xCur = newY % yVol
            newY = yVol
        else:
            xCur = 0

        ans = self.dfs(xVol, xCur, yVol, newY, target, visited)
        if ans:
            return ans

        #Transfery y to x
        newX = xCur + yCur
        if newX > xVol:
            yCur = newX % xVol
            newX = xVol
        else:
            yCur = 0

        ans = self.dfs(xVol, newX, yVol, yCur, target, visited)
        if ans:
            return ans

        return False


sol = Solution()

print(sol.canMeasureWater(3,5,4))
print(sol.canMeasureWater(3,7,2))
print(sol.canMeasureWater(2,6,5))
print(sol.canMeasureWater(1,2,3))
