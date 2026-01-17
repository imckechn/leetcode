from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)
    
        # or 
        return heapq.nlargest(k, nums)[-1]
    
sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))