class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        largest = 0

        while left < right:
            volume = min(height[left], height[right]) * (right - left)
            largest = max(largest, volume)

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1

        return largest