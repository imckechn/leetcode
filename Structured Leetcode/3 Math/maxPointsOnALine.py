from typing import List


class Solution:
    def isInside(a, b, c):
        if (b[0] - a[0])*(c[1] - a[1]) == (b[1] - a[1])*(c[0] - a[0]):
            return True
        return False


    def maxPoints(self, points: List[List[int]]) -> int:
        checkedPoints = []
        largest = 1

        for pointA in points:
            for pointB in points:
                if pointA == pointB:
                    continue
                for c in checkedPoints:
                    if pointA in c and pointB in c:
                        continue
                
                insidePoints = [pointA, pointB]
                for pointC in points:
                    if pointC == pointA or pointC == pointB:
                        continue
                    if Solution.isInside(pointA, pointB, pointC):
                        insidePoints.append(pointC)

                if len(insidePoints) > largest:
                    largest = len(insidePoints)

                checkedPoints.append(insidePoints)

        return largest
    
print(Solution.maxPoints(None, [[1,1],[2,2],[3,3]]))
print(Solution.maxPoints(None, [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))