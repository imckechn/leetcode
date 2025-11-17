import math
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        high = len(nums) - 1
        low = 0

        if high == -1:
            return [-1,-1]
        if high == 0:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return [
                    self.searchLeft(nums[:mid+1], target),
                    mid + self.searchRight(nums[mid:], target)
                ]

            elif nums[mid] < target:
                low = mid + 1
            
            else:
                high = mid - 1

        return [-1,-1]


    def searchRight(self, nums, target):
        high = len(nums) - 1
        low = 0

        if high == 0:
            return 0

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target and (mid == high or  nums[mid+1] != target):
                return mid
            
            elif nums[mid] != target:
                high = mid - 1
            
            else:
                low = mid + 1
                
        return low

    def searchLeft(self, nums, target):
        high = len(nums) - 1
        low = 0

        if high == 0:
            return 0

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target and (mid == 0 or mid-1 >= 0 and nums[mid-1] != target):
                return mid
            
            elif nums[mid] != target:
                low = mid + 1
            
            else:
                high = mid - 1

        return high
    
sol = Solution()

nums = [5,7,7,7,8,8,10]
target = 5
expected = [0,0]

ans = sol.searchRange(nums, target)
if ans == expected:
    print("passed")
else:
    print("Failed, got " + str(ans))


nums = [5,7,7,7,8,8,10]
target = 7
expected = [1,3]

ans = sol.searchRange(nums, target)
if ans == expected:
    print("passed")
else:
    print("Failed, got " + str(ans))


nums = [5,7,7,7,8,8,10]
target = 6
expected = [-1,-1]

ans = sol.searchRange(nums, target)
if ans == expected:
    print("passed")
else:
    print("Failed, got " + str(ans))


nums = [5,7,7,7,8,8,10]
target = 10
expected = [6,6]

ans = sol.searchRange(nums, target)
if ans == expected:
    print("passed")
else:
    print("Failed, got " + str(ans))


nums = [1]
target = 0
expected = [-1,-1]

ans = sol.searchRange(nums, target)
if ans == expected:
    print("passed")
else:
    print("Failed, got " + str(ans))


nums = [2,2]
target = 2
expected = [0,1]

ans = sol.searchRange(nums, target)
if ans == expected:
    print("passed")
else:
    print("Failed, got " + str(ans))

nums = [1]
target = 1
expected = [0,0]

ans = sol.searchRange(nums, target)
if ans == expected:
    print("passed")
else:
    print("Failed, got " + str(ans))

nums = [1,2,2,3,4,4,4]
target = 4
expected = [4,6]

ans = sol.searchRange(nums, target)
if ans == expected:
    print("passed")
else:
    print("Failed, got " + str(ans))