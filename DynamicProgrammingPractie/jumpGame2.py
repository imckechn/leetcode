from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool: #Should be able to take a greedy approach to jumping
        if len(nums) == 1 or len(nums) == 0:
            return 0
        elif nums[0] >= len(nums) -1:
            return 1

        far = nums[0]
        jumpCount = 1       
        nextFarthest = nums[0] + nums[far]

        for i in range(1, len(nums)):
            if nums[i] + i >= nextFarthest:
                nextFarthest = nums[i] + i

            if nextFarthest >= len(nums) - 1:
                return jumpCount+1

            if i == far:
                jumpCount += 1
                far = nextFarthest
                nextFarthest = nums[i] + i + 1
                
                if far >= len(nums) - 1:
                    return jumpCount

        return jumpCount

                    
# print(Solution.canJump(None,  [0])) #8
print(Solution.canJump(None,  [1,2,3])) #8
