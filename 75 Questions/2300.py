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