from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool: #Should be able to take a greedy approach to jumping
        if len(nums) == 1 or len(nums) == 1:
            return 1

        far = nums[0]
        jumpCount = 1
        nextFarthest = nums[0] + nums[far]

        if far == len(nums) - 1:
            return jumpCount

        for i in range(1, len(nums)):
            if i == far:
                far = nextFarthest
                nextFarthest = nums[i] + i + 1
                jumpCount += 1

            if nums[i] + i >= nextFarthest:
                nextFarthest = nums[i] + i

            if nextFarthest == len(nums) - 1:
                return jumpCount +1

        return jumpCount

                    
print(Solution.canJump(None,  [2,1])) #8
print(Solution.canJump(None,  [1,1,1, 1,1,1, 1,1,1])) #8
print(Solution.canJump(None,  [2,3,1,1,4])) #2
print(Solution.canJump(None,  [3,2,2,0,4])) #2
print(Solution.canJump(None,  [2,0,0])) #1
print(Solution.canJump(None,  [2,3,0,1,4])) #2

