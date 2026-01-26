class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = [nums[0]]
        rsum = 0
        indexFound = -1

        for i in range(1, len(nums)):
            lsum.append(lsum[-1] + nums[i])

        for i in range(len(nums)-1, -1, -1):
            rsum += nums[i]
            
            if rsum == lsum[i]:
                indexFound = i
        return indexFound
