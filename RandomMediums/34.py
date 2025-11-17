import math
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = math.ceil(len(nums)/2)
        change = 1
        length = len(nums)

        if length == 0:
            return [-1,-1]
        if length == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]

        while change != 0 and index < length:
            change = math.ceil(index/2)
            if nums[index] == target:
                return [
                    self.searchLeft(nums[:index+1], target),
                    index + self.searchRight(nums[index:], target)
                ]

            elif nums[index] > target:
                index -= change
            
            else:
                index += change

        return [-1,-1]


    def searchRight(self, nums, target):
        length = len(nums)
        index = math.ceil(length/2)
        change = 1

        if length == 1:
            return 0

        while change != 0 and index < length:
            change = math.ceil(index/2)
            if nums[index] == target and (index == length - 1 or  nums[index+1] != target):
                return index
            
            elif nums[index] != target:
                index -= change

            else: index += change

        return 0

    def searchLeft(self, nums, target):
        length = len(nums)
        index = math.ceil(length/2)
        change = 1

        if length == 1:
            return 0

        while change != 0 and index < length:
            change = math.ceil(index/2)
            if nums[index] == target and (index == 0 or index-1 >= 0 and nums[index-1] != target):
                return index
            
            elif nums[index] != target:
                index += change

            else: index -= change

        return length-1
    
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