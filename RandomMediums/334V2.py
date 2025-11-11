from cmath import inf
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = inf
        second = inf

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
            
        return False


        

sol = Solution()

#Test 1
input = [20,100,10,12,5,13]
expected = True
ans = sol.increasingTriplet(input)

if ans != expected:
    print("T1 Failed")
else:
    print("T1 Passed")

#Test 2
input = [5,4,3,2,1]
expected = False
ans = sol.increasingTriplet(input)

if ans != expected:
    print("T2 Failed")
else:
    print("T2 Passed")

#Test 3
input = [2,1,5,0,4,6]
expected = True
ans = sol.increasingTriplet(input)

if ans != expected:
    print("T3 Failed")
else:
    print("T3 Passed")