from typing import List


class Solution:
    def __init__(self):
        self.permutations = []

    def perm(self, nums, len):
        if len == 1:
            if nums not in self.permutations:
                self.permutations.append(nums.copy())
            return

        self.perm(nums, len - 1)
        for i in range(len-1):
            if len % 2 == 0:
                nums[i], nums[len-1] = nums[len-1], nums[i]
            else:
                nums[0], nums[len-1] = nums[len-1], nums[0]
            self.perm(nums, len - 1)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        self.perm(nums, len(nums))
        return self.permutations

sol = Solution()
# print(sol.permuteUnique([1,2,3,4,5]))
# sol = Solution()
print(sol.permuteUnique([1,1,2]))