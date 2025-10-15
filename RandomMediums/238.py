from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        total = 1

        for i in range(1, len(nums)):
            total *= nums[i-1]
            answer[i] *= total

            
        total = 1
        for i in range(len(nums)-2, -1, -1):
            total *= nums[i+1]
            answer[i] *= total

        return answer
    
Solution.productExceptSelf(None, [1,2,3,4])