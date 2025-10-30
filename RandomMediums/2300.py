import bisect
from heapq import _heapify_max, _heappop_max
import math
from typing import List



class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        answer = []

        left = 0
        right = len(potions)-1

        for i in range(len(spells)):
            spell = spells[i]
            minimumSpell = math.ceil(success/spell)
            leftPointer = left
            rightPointer = right

            if minimumSpell > potions[-1]:
                answer.append(0)
                continue
            elif minimumSpell <= potions[0]:
                answer.append(len(potions))
                continue

            while leftPointer < rightPointer:
                mid = leftPointer + math.ceil( (rightPointer-leftPointer) / 2)

                if potions[mid] == minimumSpell or (potions[mid] > minimumSpell and potions[mid-1] < minimumSpell):
                    if potions[mid] == minimumSpell:
                        while potions[mid-1] == potions[mid]:
                            mid -= 1
                    answer.append(len(potions) - mid)
                    break

                elif potions[mid] > minimumSpell:
                    rightPointer = mid

                else:
                    leftPointer = mid

            if len(answer) != i+1:
                answer.append(len(potions) - mid)

        return answer


sol = Solution()

# Test 1
spells = [5,1,3]
potions = [1,2,3,4,5,6,7]
success = 7
expected = [6,1,5]
answer = sol.successfulPairs(spells, potions, success)

if answer == expected:
    print("Test 1 passed")
else:
    print("Test 1 failed, got " + str(answer))

#Test 2
spells = [3,1,2]
potions = [8,5,8]
success = 16
expected = [2,0,2]
answer = sol.successfulPairs(spells, potions, success)

if answer == expected:
    print("Test 2 passed")
else:
    print("Test 2 failed, got " + str(answer))

#Test 3
spells = [15,8,19]
potions = [38,36,23]
success = 328
expected = [3,0,3]
answer = sol.successfulPairs(spells, potions, success)

if answer == expected:
    print("Test 3 passed")
else:
    print("Test 3 failed, got " + str(answer))
