from typing import List

class Solution:
    def findTriplet(factors, nums):
        triplets = 0

        for pair in factors:
            a = 0
            b = 0
            for i in range(len(nums)):
                if nums[i] == pair[0]:
                    a += 1
                
                elif nums[i] == pair[1]:
                    b += 1

            if pair[0] == pair[1] and a > 1: #Issue is here
                triplets += int(a/2)
            else:
                triplets += a * b

        return triplets

    
    def findFactors(number):
        factors = [[1, number]]
        for i in range(2, number//2):
            factor = int(number/i)
            if number == i * factor:
                factors.append([i, factor])

        return factors


    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        triplets = 0
        nums1.sort()
        nums2.sort()

        for num in nums1:
            factors = Solution.findFactors(num * num)
            triplets += Solution.findTriplet(factors, nums2)

        # for num in nums2:
        #     factors = Solution.findFactors(num * num)
        #     triplets += Solution.findTriplet(factors, nums1)


        return triplets

# print(Solution.numTriplets(None, [7,4], [5,2,8,9])) # 1
print(Solution.numTriplets(None, [1,1], [1,1,1])) #9
print(Solution.numTriplets(None, [7,7,8,3], [1,2,9,7])) #2
 