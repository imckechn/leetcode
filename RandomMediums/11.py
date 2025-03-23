from typing import List


class Solution:
    def getVolume(arr, a, b):
        width = b - a
        height = min(arr[a], arr[b])
        return width * height


    def maxArea(self, height: List[int]) -> int:
        maxVol = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                vol = Solution.getVolume(height, i, j)

                if vol > maxVol:
                    maxVol = vol

        return maxVol
        