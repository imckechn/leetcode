from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool: #Should be able to take a greedy approach to jumping
        return Solution.canJump2(self, nums, 0, 0, [0])

        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False  # Cannot proceed further
            maxReach = max(maxReach, i + nums[i])
            if maxReach >= len(nums) - 1:
                return True  # Reached or surpassed last index
        return False
    
    def canJump2(self, nums, i, maxReach, indexes): #Should be able to take a greedy approach to jumping
        for i in range(i, len(nums)):
            if i > maxReach:
                return False  # Cannot proceed further
            
            maxReach = min(Solution.canJump2(self, nums, i+1, maxReach, indexes), Solution.canJump2(self, nums, i + nums[i], maxReach, indexes))

            if maxReach >= len(nums) - 1:
                return len(indexes)  # Reached or surpassed last index
        return len(nums) + 1
                    
# print(Solution.canJump(None,  [1,1,1,1,1,1,1,1,1])) #True
# print(Solution.canJump(None,  [2,3,1,1,4])) #True
print(Solution.canJump(None,  [3,2,2,0,4])) #False
print(Solution.canJump(None,  [2,0,0])) #True
print(Solution.canJump(None,  [2,3,1,1,4])) #2
print(Solution.canJump(None,  [2,3,0,1,4])) #2

