from typing import List, Optional

class Solution:
    def backTrack(nums, frozenIndex):
        nums = nums.copy()
        if frozenIndex+2 >= len(nums):
            return [nums.copy()]

        solutions = []

        for i in range(frozenIndex+1, len(nums)):
            temp = nums[frozenIndex+1]
            nums[frozenIndex+1] = nums[i]
            nums[i] = temp

            solutions += Solution.backTrack(nums, frozenIndex+1)
        
        return solutions

    def permute(self, nums: List[int]) -> List[List[int]]:
        solutions = []

        for i in range(len(nums)):
            temp = nums[0]
            nums[0] = nums[i]
            nums[i] = temp

            solutions += Solution.backTrack(nums, 0)
            temp = nums[0]
            nums[0] = nums[i]
            nums[i] = temp

        
        return solutions

# print(Solution.permute(None, [1,2,3])) 
print(Solution.permute(None, [1])) 