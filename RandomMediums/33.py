from math import floor
import math
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        elif len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1

        #Find pivot index
        pivotFound = False

        pivotIndex = len(nums)//2
        while True:
            if (pivotIndex == 0 and nums[0] < nums[pivotIndex]) or (pivotIndex == len(nums)-1):
                break

            elif nums[pivotIndex] > nums[pivotIndex+1] and nums[pivotIndex] > nums[pivotIndex-1]:
                pivotFound = True
                break

            if nums[pivotIndex] > nums[0]:
                pivotIndex += math.ceil(pivotIndex/2)
            else:
                pivotIndex -= math.ceil(pivotIndex/2)

        searchSet = nums
        otherSetLength = 0
            
        if pivotFound:
            #If it's within left of pivot
            if target >= nums[0] and target <= nums[pivotIndex]:
                searchSet = nums[:pivotIndex+1]
            else:
                otherSetLength = len(nums[:pivotIndex+1])
                searchSet = nums[pivotIndex+1:]

        index = len(searchSet)//2
        prevIndex = -1
        prevPrevIndex = -1
        while True:
            if index >= len(searchSet):
                return -1

            if target == searchSet[index]:
                return index + otherSetLength
            
            prevPrevIndex = prevIndex
            prevIndex = index
            if target > searchSet[index]:
                index += math.ceil(index/2)

            else:
                index = index//2

            if prevIndex == index or prevPrevIndex == index:
                return -1


sol = Solution()

#Test 1
nums = [5,1,3]
target = 0
expected = -1

ans = sol.search(nums, target)
if ans != expected:
    print("Failed")
else:
    print("Passed")

#Test 1
nums = [4,5,6,7,0,1,2]
target = 0
expected = 4

ans = sol.search(nums, target)
if ans != expected:
    print("Failed")
else:
    print("Passed")

#Test 
nums = [4,5,6,7,0,1,2]
target = 4
expected = 0

ans = sol.search(nums, target)
if ans != expected:
    print("Failed")
else:
    print("Passed")

#Test 
nums = [4,5,6,7,0,1,2]
target = 2
expected = 6

ans = sol.search(nums, target)
if ans != expected:
    print("Failed")
else:
    print("Passed")

#Test 2
nums = [4,5,6,7,0,1,2]
target = 3
expected = -1

ans = sol.search(nums, target)
if ans != expected:
    print("Failed")
else:
    print("Passed")

#Test 3
nums = [1]
target = 0
expected = -1

ans = sol.search(nums, target)
if ans != expected:
    print("Failed")
else:
    print("Passed")

#Test 3
nums = [1,3,5]
target = 4
expected = -1

ans = sol.search(nums, target)
if ans != expected:
    print("Failed")
else:
    print("Passed")