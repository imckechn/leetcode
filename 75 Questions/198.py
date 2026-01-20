class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums[0], nums[-1])
        
        else:
            self.sequence = [nums[0], nums[1], nums[0] + nums[2]]

        for i in range(3, len(nums)):
            self.sequence.append(max(nums[i] + self.sequence[-2], nums[i] + self.sequence[-3]))

        return max(self.sequence[-1], self.sequence[-2])