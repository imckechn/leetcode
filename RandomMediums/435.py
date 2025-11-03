from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        i = 0
        count = 0

        while i < len(intervals)-1:
            if intervals[i][0] == intervals[i+1][0]:
                if intervals[i][1] >= intervals[i+1][1]:
                    intervals.pop(i)
                else:
                    intervals.pop(i+1)

                count += 1
                continue

            elif intervals[i][1] > intervals[i+1][0]:
                len1 = intervals[i][1] - intervals[i][0]
                len2 = intervals[i+1][1] - intervals[i+1][0]

                if len2 >= len1:
                    intervals.pop(i+1)
                else:
                    intervals.pop(i)

                count += 1
                continue
            else:
                i += 1
        return count

sol = Solution()

#Test 0
intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
expected = 7
answer = sol.eraseOverlapIntervals(intervals)

if answer == expected:
    print("Test 0 passed")
else:
    print("Test 0 failed")

#Test 1
intervals = [[1,2],[2,3],[3,4],[1,3]]
expected = 1
answer = sol.eraseOverlapIntervals(intervals)

if answer == expected:
    print("Test 1 passed")
else:
    print("Test 1 failed")

#Test 2
intervals = [[1,2],[1,2],[1,2]]
expected = 2
answer = sol.eraseOverlapIntervals(intervals)

if answer == expected:
    print("Test 2 passed")
else:
    print("Test 2 failed")

#Test 3
intervals = [[1,2],[2,3]]
expected = 0
answer = sol.eraseOverlapIntervals(intervals)

if answer == expected:
    print("Test 3 passed")
else:
    print("Test 3 failed")