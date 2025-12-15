from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest = 0
        for candy in candies:
            largest = max(largest, candy)
        
        ans = []
        for candy in candies:
            if candy + extraCandies >= largest:
                ans.append(True)
            else:
                ans.append(False)
        return ans