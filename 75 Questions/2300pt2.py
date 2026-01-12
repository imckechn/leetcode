import bisect
import math
from typing import List

class Solution:
    def betterSol(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        answer = []
        pLen = len(potions)

        for spell in spells:
            target = math.ceil(success/spell)
            answer.append(pLen-bisect.bisect_left(potions, target))
        return answer

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        answer = []

        for spell in spells:
            answer.append(self.bSearch(spell, potions, success))
        return answer
    
    def bSearch(self, spell, potions, goal):
        potionLength = len(potions)
        low = 0
        high = potionLength-1
        highestIndex = high+1

        while low <= high:
            mid = (high+low)//2

            if spell * potions[mid] >= goal:
                highestIndex = mid
                high = mid-1
            else:
                low = mid+1

        return potionLength - highestIndex
    
sol = Solution()
print(sol.betterSol([5,1,3], [1,2,3,4,5], 7))