from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        end = intervals[0][1]
        count = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
        return count

sol = Solution()
print(sol.eraseOverlapIntervals([[-24,99],[96,98],[71,96],[88,99],[-24,4],[99,100],[-69,-27],[18,28],[25,38],[8,25],[-99,33],[-85,-30],[56,64],[-77,98],[-38,88],[-96,6],[91,92],[-39,80],[-7,97],[-82,9],[-80,3],[87,94],[-96,16],[-15,40],[-40,86],[31,81],[97,98],[69,83],[-40,47],[1,82],[13,44],[-92,-65],[51,80]])) #9
print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))