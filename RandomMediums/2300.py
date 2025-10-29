from heapq import _heapify_max, _heappop_max
import math
from typing import List



class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        potions = potions.copy()
        answer = []

        midIndex = math.ceil(len(potions)/2)

        for spell in spells:
            index = midIndex
            count = 0
            minValue = math.ceil(success/spell)
            value = math.ceil(index/2)

            if minValue > potions[-1]:
                answer.append(count)
                continue
            elif minValue < potions[0]:
                answer.append(len(potions))
                continue

            while True:
                if potions[index] >= minValue and potions[index-1] < minValue:
                    break

                if potions[index] < minValue:
                    index = index + value
                    if index == 0:
                        index += 1

                else:
                    index = index - value

                value = math.ceil(value/2)
            answer.append(len(potions)-index)
        return answer
    

sol = Solution()

# #Test 1
# spells = [5,1,3]
# potions = [1,2,3,4,5,6,7]
# success = 7
# expected = [6,1,5]
# answer = sol.successfulPairs(spells, potions, success)

# if answer == expected:
#     print("Test 1 passed")
# else:
#     print("Test 1 failed, got " + str(answer))

# #Test 2
# spells = [3,1,2]
# potions = [8,5,8]
# success = 16
# expected = [2,0,2]
# answer = sol.successfulPairs(spells, potions, success)

# if answer == expected:
#     print("Test 2 passed")
# else:
#     print("Test 2 failed, got " + str(answer))

# #Test 3
# spells = [15,8,19]
# potions = [38,36,23]
# success = 328
# expected = [3,0,3]
# answer = sol.successfulPairs(spells, potions, success)

# if answer == expected:
#     print("Test 3 passed")
# else:
#     print("Test 3 failed, got " + str(answer))

#Test 4
spells = [1,30,13,35,36,35,10,32,35,1,20,32,37,39,31,28,12,5,5,11,25,25,20,10,34,9,9,24,13,26,13,5,24,20,29,35,31,5,29,29,24,11,16,8,29,7,6,19,18,14,34,1,16,34,40,2,27,39,5,20,34,34,20,16,22,22,25,31,33,39,35,36,17,37,19,8,34,36,39,6,22]
potions = [39,16,37,31,9,33,14,23,32,36,17,35,34]
success = 898
expected = [3,0,3]
answer = sol.successfulPairs(spells, potions, success)

if answer == expected:
    print("Test 4 passed")
else:
    print("Test 4 failed, got " + str(answer))
