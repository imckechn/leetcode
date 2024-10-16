class Solution:
    def findMinArrowShots(points):
        points = sorted(points, key= lambda interval: (interval[0], interval[0]))
        
        i = 0
        while i < len(points) - 1:
            if points[i][1] >= points[i+1][0]:
                newInterval = [
                    max(points[i][0], points[i+1][0]), 
                    min(points[i][1], points[i+1][1])
                ]
                points.pop(i+1)
                points[i] = newInterval
            
            else:
                i += 1

        return len(points)
        
print(Solution.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(Solution.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(Solution.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))