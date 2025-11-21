from typing import List
import heapq

#Need to try keeping track of smallest and largest elements in heaps. This should reduce the complexity.
# Sliding window approach was right but needed to us heaps instead of regular searching 


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        numsLength = len(nums)
        if numsLength <= 1:
            return numsLength
        
        count = 1
        left = 0
        right = 0
        minHeap = heapq.heapify(nums[0])
        maxHeap = heapq.heapify_max(nums[0])


        while right < numsLength:

            #Expand window to the right
            if largest - smallest <= limit:
                right += 1

                if right-left > count:
                    count = (right - left)

                if right == numsLength:
                    break

            #reduce window size from right 
            #Make sure left != right
            else:
                if nums[left] == minHeap[0]:
                    


        return count
    
sol = Solution()

ans =  sol.longestSubarray([8,2,4,7], 4)
if ans != 2:
    print("Failed got " + str(ans))
else:
    print("Passed")

ans =  sol.longestSubarray([10,1,2,4,7,2], 5)
if ans != 4:
    print("Failed got " + str(ans))
else:
    print("Passed")

ans =  sol.longestSubarray([4,2,2,2,4,4,2,2], 0)
if ans != 3:
    print("Failed got " + str(ans))
else:
    print("Passed")

