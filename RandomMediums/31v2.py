from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        length = len(nums)-1
        smallestIndex = length
        swapMade = False

        for i in range(length, 0, -1):
            if nums[i] < nums[smallestIndex]:
                smallestIndex = i

            if nums[i] > nums[i-1]:
                swapMade = True
                nums[i-1], nums[smallestIndex] = nums[smallestIndex], nums[i-1]

                subset = nums[i:]
                subset.sort()
                nums = nums[:i] + subset
                break

        if not swapMade:
            nums.reverse()
        return nums

sol = Solution()
# print(sol.nextPermutation([1,2,3,4])) #1,2,4,3
# print(sol.nextPermutation([1,4,3,2])) #2,1,3,4
# print(sol.nextPermutation([3,2,1,4])) #3,2,4,1
# print(sol.nextPermutation([4,3,2,1])) #1,2,3,4
print(sol.nextPermutation([1,3,2])) #[2,1,3]

        