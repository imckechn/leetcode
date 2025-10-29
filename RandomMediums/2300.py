from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort(reverse=True)
        answer = []

        for spell in spells:
            count = 0

            for potion in potions:
                if spell * potion >= success:
                    count += 1
                else:
                    break
            
            answer.append(count)
        return answer
    

sol = Solution()

#Test 1
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
expected = [4,0,3]
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
    print("Test 1 passed")
else:
    print("Test 1 failed, got " + str(answer))
