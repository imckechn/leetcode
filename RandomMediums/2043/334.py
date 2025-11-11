from cmath import inf
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        prev = inf

        for i in range(len(nums)):
            if nums[i] < prev:
                ans = self.findTrip(nums[i:], nums[i], 2)

                if ans:
                    return ans
                else:
                    prev = nums[i]
        return False



    def findTrip(self, nums, nextSmallest, depth):
        if depth == 0:
            return True
        prev = inf

        for i in range(len(nums)):
            if nums[i] > nextSmallest and nums[i] < prev:
                ans = self.findTrip(nums[i:], nums[i], depth-1)

                if ans:
                    return ans
                else:
                    prev = nums[i]

        return False


        

sol = Solution()

#Test 1
input = [1,2,3,4,5]
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