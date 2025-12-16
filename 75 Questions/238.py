from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftToRight = [1]
        ans = []
        for i in range(len(nums)):
            leftToRight.append(leftToRight[i] * nums[i])

        nums.append(1)
        sum = 1
        answer = []
        for i in range(len(nums)-2, -1, -1):
            answer.append(leftToRight[i] * sum)
            sum *= nums[i]

        answer.reverse()
        return answer

sol= Solution()
input = [1,2,3,4]
expected = [24,12,8,6]

sol.productExceptSelf(input)