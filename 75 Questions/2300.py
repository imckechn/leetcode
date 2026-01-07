import math
from typing import List


class Solution:
    potionsLength = 0

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        self.potionsLength = len(potions)
        successses = []

        for spell in spells:
            index = self.bSearch(spell, potions, success)
            successses.append(self.potionsLength - index if index != -1 else 0)
        return successses

    def bSearch(self, spell, potions, g):
        low, mid = 0, 0
        high = self.potionsLength-1
        index = -1

        while low <= high:
            mid = (low+high)//2
            if spell*potions[mid] >= g:
                index = mid
                high = mid-1
            else:
                low = mid+1

        return index


sol = Solution()
# sol.successfulPairs([15,39,38,35,33,25,31,12,40,27,29,16,22,24,7,36,29,34,24,9,11,35,21,3,33,10,9,27,35,17,14,3,35,35,39,23,35,14,31,7], [25,19,30,37,14,30,38,22,38,38,26,33,34,23,40,28,15,29,36,39,39,37,32,38,8,17,39,20,4,39,39,7,30,35,29,23],317)
sol.successfulPairs([3,1,2], [8,5,8], 16)
sol.successfulPairs([5,1,3], [1,2,3,4,5], 7)
sol.successfulPairs([40,35,20,15,30,15,8,15,18,28,25,36,18,7,24,11,29,16,29,10,29,23,11,20,33,13,20,16,7,4,32,15,28,4,11,24,21,21,16,30,3,30,25,5], [9,2,3,2,26,9,15,23,6,1,10,11,11,16,5,21,18,36,25,30,27,39,34,8,9,2], 860)