from typing import List


class Solution:
    def crawl(nums, position):
        smallest, biggest = position, position
        for i in range(position, len(nums)):
            if nums[i] != nums[position]:
                biggest = i-1
                break
            biggest = i


        for i in range(position, 0, -1):
            if nums[i] != nums[position]:
                smallest = i+1
                break
            smallest = i

        return [smallest, biggest]


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        
        if len(nums) == 2:
            if nums[0] == target:
                return Solution.crawl(nums, 0)
            elif nums[1] == target:
                return Solution.crawl(nums, 1)
            return [-1,-1]

        start = 0
        end = len(nums)-1
        
        while True:
            mid = (end - start) // 2 + start

            if nums[mid] == target:
                return Solution.crawl(nums, mid)
            elif start+1 == end:
                return [-1,-1]
            
            if target < nums[mid]:
                end = mid
            else:
                start = mid

# print(Solution.searchRange(None, [5,7,7,8,8,10], 8))
# print(Solution.searchRange(None, [5,7,7,8,8,10], 6))
# print(Solution.searchRange(None, [1], 1))
# print(Solution.searchRange(None, [2, 2], 2))
print(Solution.searchRange(None, [1, 2, 3], 3))