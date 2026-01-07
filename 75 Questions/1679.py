from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0

        if len(nums) == 0:
            return 0
        
        lp = 0
        rp = len(nums)-1

        while lp < rp:
            if nums[lp] + nums[rp] == k:
                count += 1
                lp += 1
                rp -= 1

            elif nums[lp] + nums[rp] < k:
                lp += 1

            else:
                rp -= 1

        return count