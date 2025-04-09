from typing import List


class Solution:
    def heaps(nums, k):
        if k == 1:
            print(nums)
            return nums
        
        Solution.heaps(nums, k-1)
        # print(nums)

        for i in range(k-1):
            if k % 2 == 0:
                nums[i], nums[k-1] = nums[k-1], nums[i]
            else:
                nums[0], nums[k-1] = nums[k-1], nums[0]

            Solution.heaps(nums, k-1)
            # print(nums)

        return nums



    def nextPermutation(self, nums: List[int]) -> None:
        return Solution.heaps(nums, len(nums))
        """
        Do not return anything, modify nums in-place instead.
        """
        
sol = Solution()

sol.nextPermutation([1,2,3,4])

# 1,2,3 -> half way plus one
# 1,2,3,4 -> half way plus two
