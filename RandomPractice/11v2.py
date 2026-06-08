from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        vol = 0

        while right > left:

            vol = max(vol, (right-left) * min(height[right], height[left]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return vol
        
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))