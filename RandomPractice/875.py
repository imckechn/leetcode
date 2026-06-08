import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        high = max(piles)
        low = 1
        
        while high > low:

            current = (low+high)//2

            time = 0

            for pile in piles:
                time += math.ceil(pile/current)

            if time <= h:
                high = current
            else:
                low = current+1
        return high
            
sol = Solution()
# print(sol.minEatingSpeed([312884470], 312884469)) #ans = 4
print(sol.minEatingSpeed([30,11,23,4,20], 5)) #ans = 4
print(sol.minEatingSpeed([3,6,7,11], 8)) #ans = 4