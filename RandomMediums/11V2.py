from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left != right:
            area = (right - left) *  min(height[left], height[right])

            if area > maxArea:
                maxArea = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

if Solution.maxArea(None, [1,8,6,2,5,4,8,3,7]) != 49:
    print("Test 1 Failed")
else:
    print("Test 1 passed")

if Solution.maxArea(None, [1,2,4,3]) != 4:
    print("Test 1 Failed")
else:
    print("Test 1 passed")