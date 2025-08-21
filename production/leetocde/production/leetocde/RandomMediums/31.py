from typing import List

# To solve
# 1. Find first decreasing element starting at the right side of the list
# 2. Find the smallest element from the RHS that is greater than the first decreasing element
# 3. Swap the two elements
# 4. Reverse the sublist from the first decreasing element to the end of the list


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Should try a backtracking approach https://medium.com/@hanxuyang0826/mastering-backtracking-from-leetcode-to-real-world-applications-4c9150de20da
        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return
        
        j = len(nums) - 1
        while j >= i and nums[j] <= nums[i-1]:
            j -= 1
        
        nums[i-1], nums[j] = nums[j], nums[i-1]

        nums[i:] = reversed(nums[i:])



        

        
sol = Solution()

sol.nextPermutation([1,3,2]) #2,1,3
# sol.nextPermutation([1,2,3,4,5])

# 1,2,3 -> half way plus one
# 1,2,3,4 -> half way plus two
