class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seenCount = 1
        elem = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == elem:
                if seenCount >= 2:
                    nums.pop(i)
                    i -= 1
                seenCount += 1

            elif nums[i] != elem:
                elem = nums[i]
                seenCount = 1
            i += 1