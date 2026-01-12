from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        mid = left

        while left <= right:
            mid = (left+right)//2

            if mid > 0 and nums[mid-1] > nums[mid]:
                right = mid-1

            elif mid < len(nums)-1 and nums[mid+1] > nums[mid]:
                left = mid+1
            
            else:
                break
        
        return mid


sol = Solution()
print(sol.findPeakElement([1,2]))
print(sol.findPeakElement([1,2,3,1]))