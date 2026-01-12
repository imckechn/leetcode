import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        low = 1
        high = piles[-1]
        answer = high

        while low <= high:
            mid = (low+high)//2

            count = 0
            for pile in piles:
                count += math.ceil(pile/mid)

            if count <= h:
                answer = min(answer, mid)
                high = mid-1

            else:
                low = mid+1
        return answer

sol = Solution()
print(sol.minEatingSpeed([3,6,7,11], 8))