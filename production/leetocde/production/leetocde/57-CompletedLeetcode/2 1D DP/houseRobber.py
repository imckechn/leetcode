from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        prev1 = 0
        prev2 = 0

        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = temp

        return prev1


print(Solution.rob(None, [1,2,3,1]))
print(Solution.rob(None, [2,7,9,3,1]))
print(Solution.rob(None, [1,2]))
print(Solution.rob(None, [2,3,2]))