from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0

        optimal = {}

        for i in range(len(nums)-1, -1, -1):
            if i+2 in optimal and i+1 in optimal:
                optimal[i] = max(nums[i] + optimal[i+2], optimal[i+1])

            elif i+2 in optimal:
                optimal[i] = nums[i] + optimal[i+2]

            elif i+1 in optimal:
                optimal[i] = max(optimal[i+1], nums[i])

            else:
                optimal[i] = nums[i]

        return max(optimal[0], optimal[1])
    
sol = Solution()
print(sol.rob([2,1,1,2]))
print(sol.rob([2,7,9,3,1]))
print(sol.rob([1,2,3,1]))