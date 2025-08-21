from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        localMax = nums[0]
        globalMax = nums[0]

        for i in range(1, len(nums)):
            if localMax + nums[i] > nums[i]:
                localMax += nums[i]

            else:
                localMax = nums[i]

            if localMax > globalMax:
                globalMax = localMax

        return globalMax

print(Solution.maxSubArray(None, [8,-19,5,-4,20]))