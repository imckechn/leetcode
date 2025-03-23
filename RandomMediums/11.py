from typing import List


class Solution:
    def getVolume(height, leftPointer, rightPointer):
        width = rightPointer - leftPointer
        height = min(height[leftPointer], height[rightPointer])
        return width * height


    def maxArea(self, height: List[int]) -> int:
        maxVol = 0

        leftPointer = 0
        rightPointer = len(height) - 1

        while True:
            if leftPointer == rightPointer:
                break

            vol = Solution.getVolume(height, leftPointer, rightPointer)
            if vol > maxVol:
                maxVol = vol

            if height[leftPointer] > height[rightPointer] and height[leftPointer] > height[rightPointer-1]:
                rightPointer -= 1
            
            elif height[rightPointer] > height[leftPointer] and height[rightPointer] > height[leftPointer+1]:
                leftPointer += 1

            elif height[leftPointer+1] < height[rightPointer-1]:
                rightPointer -= 1
            else:
                leftPointer += 1

        return maxVol

print(Solution.maxArea(None, [3,6,1]))
print(Solution.maxArea(None, [1,2,4,3]))
print(Solution.maxArea(None, [1,8,6,2,5,4,8,3,7]))