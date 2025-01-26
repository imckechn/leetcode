from typing import List


class Solution:
    def checkHalf(nums, start, end, target):
        if nums[start] == target:
            return start
        
        splitIndex = int((end-start)/2) + start

        if nums[splitIndex] == target:
            return splitIndex
        
        if len(nums[start:end]) == 1:
            return -1

        if target <= nums[start]: 
            if target <= nums[splitIndex]:
                return Solution.checkHalf(nums, start, splitIndex, target)
            return Solution.checkHalf(nums, splitIndex, len(nums), target)

        elif target >= nums[start] and target < nums[splitIndex]:
            return Solution.checkHalf(nums, start, splitIndex, target)

        elif target >= nums[splitIndex]:
            return Solution.checkHalf(nums, splitIndex, len(nums), target)
        
        return -1
        

    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        
        splitIndex = int(len(nums)/2)

        if target <= nums[0]: 
            if target >= nums[splitIndex]:
                return Solution.checkHalf(nums, splitIndex, len(nums, target))


            if target <= nums[splitIndex]:
                return Solution.checkHalf(nums, splitIndex, len(nums), target)
            return Solution.checkHalf(nums, 0, splitIndex, target)
            
        elif target >= nums[0] and target < nums[splitIndex]:
            return Solution.checkHalf(nums, 0, splitIndex, target)

        elif target >= nums[splitIndex]:
            return Solution.checkHalf(nums, splitIndex, len(nums), target)

        return -1

print(Solution.search(None, [5,1,3], 3)) #2
print(Solution.search(None, [1,3,5], 5)) #2
print(Solution.search(None, [4,5,6,7,0,1,2], 0)) #4
print(Solution.search(None, [4,5,6,7,0,1,2], 3)) #-1
print(Solution.search(None, [1, 3], 3)) #expected 1