from typing import List
import heapq

#Need to try keeping track of smallest and largest elements in heaps. This should reduce the complexity.
# Sliding window approach was right but needed to us heaps instead of regular searching 


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_heap = []
        min_heap = []

        left = 0
        max_length = 0

        for right in range(len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))
            heapq.heappush(min_heap, (nums[right], right))

            # Check if the absolute difference between the maximum and minimum values in the current window exceeds the limit
            while -max_heap[0][0] - min_heap[0][0] > limit:
                # Move the left pointer to the right until the condition is satisfied.
                # This ensures we remove the element causing the violation
                left = min(max_heap[0][1], min_heap[0][1]) + 1

                # Remove elements from the heaps that are outside the current window
                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < left:
                    heapq.heappop(min_heap)

            # Update max_length with the length of the current valid window
            max_length = max(max_length, right - left + 1)

        return max_length
    
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

