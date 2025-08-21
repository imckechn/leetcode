from typing import List


class Solution:
    def crawl(nums, position):
        smallest, biggest = position, position
        for i in range(position, len(nums)):
            if nums[i] != nums[position]:
                biggest = i-1
                break
            biggest = i


        for i in range(position, -1, -1):
            if nums[i] != nums[position]:
                smallest = i+1
                break
            smallest = i

        return [smallest, biggest]


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        if len(nums) == 1:
            if nums[0] != target:
                return [-1,-1]
            return[0,0]

        start = 0
        end = len(nums)-1
        
        while True:
            mid = (end - start) // 2 + start

            if end-start == 1:
                if nums[start] == target:
                    return Solution.crawl(nums, start)
                elif nums[end] == target:
                    return Solution.crawl(nums, end)
                else:
                    return [-1,-1]

            if nums[mid] == target:
                return Solution.crawl(nums, mid)
            
            if target < nums[mid]:
                end = mid
            else:
                start = mid

# print(Solution.searchRange(None, [5,7,7,8,8,10], 8))
# print(Solution.searchRange(None, [5,7,7,8,8,10], 6))
# print(Solution.searchRange(None, [1], 1))
# print(Solution.searchRange(None, [2, 2], 2))
# print(Solution.searchRange(None, [1, 2, 3], 3))
# print(Solution.searchRange(None, [1, 3], 3))
# print(Solution.searchRange(None, [3], 3))
# print(Solution.searchRange(None, [3], 4))
print(Solution.searchRange(None, [1,1,2], 1))