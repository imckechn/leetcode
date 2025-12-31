from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height)-1
        left = 0
        maxVal = 0

        while left < right:
            maxVal = max(maxVal, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return maxVal
    

sol = Solution()
sol.maxArea([1,8,6,2,5,4,8,3,7])