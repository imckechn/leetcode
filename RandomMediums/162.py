import math
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        if len(nums) == 1:
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums)-1

        while left < right:
            mid = left + math.ceil((right-left)/2)            

            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            
            elif nums[mid-1] > nums[mid]:
                right = mid

            else:
                left = mid


sol = Solution()

# #Test 1
# nums = [1,2,3,1]
# expected = 2
# answer = sol.findPeakElement(nums)

# if answer == expected:
#     print("Test 1 passed")
# else:
#     print("Test 1 failed")


#Test 2
nums = [1,2,1,3,5,6,4]
expected = 5
answer = sol.findPeakElement(nums)

if answer == expected:
    print("Test 2 passed")
else:
    print("Test 2 failed")

