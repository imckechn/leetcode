import math
from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort()

        low = 1
        high = nums[-1]

        while low <= high:
            mid = (high+low)//2

            if high

sol = Solution()
print(sol.minimumSize([9], 2))
print(sol.minimumSize([2,4,8,2], 4))