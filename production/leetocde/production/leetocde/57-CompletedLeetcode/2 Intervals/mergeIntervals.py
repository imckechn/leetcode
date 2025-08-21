class Solution:    
    smallest = lambda a, b: a if a < b else b
    largest = lambda a, b: a if a > b else b

    def merge(intervals):
        intervals = sorted(intervals, key= lambda interval: (interval[0], interval[0]))
        
        i = 0
        while i < len(intervals) - 1:
            if (intervals[i][1] >= intervals[i+1][0] and intervals[i][1] <= intervals[i+1][1]) or intervals[i+1][0] < intervals[i][1]:
                newInterval = [
                    Solution.smallest(intervals[i][0], intervals[i+1][0]), 
                    Solution.largest(intervals[i][1], intervals[i+1][1])
                ]
                intervals.pop(i+1)
                intervals[i] = newInterval
            
            else:
                i += 1

        return intervals
    
print(Solution.merge([[2,6],[1,3],[8,10],[15,18]]))
print(Solution.merge([[1,6],[2,3],[8,10],[15,18]]))
print(Solution.merge([[1,4],[0,2],[3,5]]))