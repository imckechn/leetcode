#Probably want to take a greedy approach for this
from typing import List

class Solution:
    def minCost(self, colours: str, neededTime: List[int]) -> int:
        i = 1
        time = 0

        while i < len(colours):
            if colours[i-1] == colours[i]:
                time += min(neededTime[i-1], neededTime[i])
                neededTime[i] = max(neededTime[i-1], neededTime[i])
            i += 1
        return time
    
sol = Solution()

#Test 1
colours = "abaac"
time = [1,2,3,4,5]
expected = 3

ans = sol.minCost(colours, time)
if ans == expected:
    print("Test 1 passed")
else:
    print("failed")

#Test 2
colours = "abc"
time = [1,2,3]
expected = 0

ans = sol.minCost(colours, time)
if ans == expected:
    print("Test 2 passed")
else:
    print("failed")

#Test 3
colours = "aabaa"
time = [1,2,3,4,1]
expected = 2

ans = sol.minCost(colours, time)
if ans == expected:
    print("Test 3 passed")
else:
    print("failed")

#Test 4
colours = "aaabbbabbbb"
time = [3,5,10,7,5,3,5,5,4,8,1]
expected = 26

ans = sol.minCost(colours, time)
if ans == expected:
    print("Test 3 passed")
else:
    print("failed, got " + str(ans))