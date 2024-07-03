class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        l = len(nums)
        k = 0
        while i < l - k:
            if nums[i] == val:
                nums.pop(i)
                i -= 1
                k += 1
            i += 1

print(Solution().removeElement([3, 2, 2, 3], 3))