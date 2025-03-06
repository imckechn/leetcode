from typing import List

class Solution:
    def findTriplet(val, nums):
        triplets = 0
        val *= val

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue

                if val == nums[i] * nums[j]:
                    triplets += 1
                
                elif val < nums[i] * nums[j]:
                    continue

        return triplets

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        triplets = 0

        for num in nums1:
            triplets += Solution.findTriplet(num, nums2)

        for num in nums2:
            triplets += Solution.findTriplet(num, nums1)

        return int(triplets/2)

print(Solution.numTriplets(None, [7,4], [5,2,8,9]))
print(Solution.numTriplets(None, [1,1], [1,1,1]))
print(Solution.numTriplets(None, [7,7,8,3], [1,2,9,7]))
