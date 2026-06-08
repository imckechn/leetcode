from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0

        while i < len(intervals)-1:
            if intervals[i][0] == intervals[i+1][0] or intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
            else:
                i += 1

        return intervals
    

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
print(sol.merge([[4,7],[1,4]]))