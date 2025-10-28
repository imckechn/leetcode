from heapq import _heapify_max, heapify, heappop
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        combo = []
        sum = 0
        minSet = []

        for i in range(len(nums1)):
            combo.append((nums2[i], [nums2[i],nums1[i]]))

        for i in range(k):
            _heapify_max(combo)
            num1, num2 = heappop(combo)
            num2 = num2[1]

            minSet.append(num1)
            sum += num2
        
        return sum * min(minSet)



sol = Solution()

# #Test 1
# nums1 = [1,3,3,2]
# nums2 = [2,1,3,4]
# k = 3
# expected = 12
# ans = sol.maxScore(nums1, nums2, k)

# if ans == expected:
#     print("Test 1 passed")
# else:
#     print("Test 1 failed")


# #Test 2
# nums1 = [4,2,3 ,1,1]
# nums2 = [7,5,10,9,6]
# k = 1
# expected = 30
# ans = sol.maxScore(nums1, nums2, k)

# if ans == expected:
#     print("Test 1 passed")
# else:
#     print("Test 1 failed")


#Test 2
nums1 = [2,1,14,12]
nums2 = [11,7,13,6]
k = 3
expected = 168
ans = sol.maxScore(nums1, nums2, k)

if ans == expected:
    print("Test 1 passed")
else:
    print("Test 1 failed")
