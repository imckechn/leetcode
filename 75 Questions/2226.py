from typing import List
import math

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        candies.sort()
        high = candies[-1]
        low = 1
        mid = (high+low)//2
        best = 0
        totalShares = 0

        while low <= high:
            for candy in candies:
                totalShares += math.floor(candy/mid)

            if totalShares >= k:
                best = mid
                low = mid+1

            else:
                high = mid-1

            mid = (high+low)//2
            totalShares = 0

        return best
    
sol = Solution()
print(sol.maximumCandies([5,6,8], 3)) #5
print(sol.maximumCandies([5,6,8], 5)) #3