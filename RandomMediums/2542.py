from heapq import _heapify_max, heapify, heappop, heappush
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # combo = []
        # sum = 0
        # minSet = []

        # for i in range(len(nums1)):
        #     combo.append((nums2[i], [nums2[i],nums1[i]]))

        # for i in range(k):
        #     _heapify_max(combo)
        #     num1, num2 = heappop(combo)
        #     num2 = num2[1]

        #     minSet.append(num1)
        #     sum += num2
        
        # return sum * min(minSet)




        # Sort pair (nums1[i], nums2[i]) by nums2[i] in decreasing order.
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key = lambda x: -x[1])
        
        # Use a min-heap to maintain the top k elements.
        top_k_heap = [x[0] for x in pairs[:k]]
        top_k_sum = sum(top_k_heap)
        heapify(top_k_heap)
        
        # The score of the first k pairs.
        answer = top_k_sum * pairs[k - 1][1]
        
        # Iterate over every nums2[i] as minimum from nums2.
        for i in range(k, len(nums1)):
            # Remove the smallest integer from the previous top k elements
            # then add nums1[i] to the top k elements.
            top_k_sum -= heappop(top_k_heap)
            top_k_sum += pairs[i][0]
            heappush(top_k_heap, pairs[i][0])
            
            # Update answer as the maximum score.
            answer = max(answer, top_k_sum * pairs[i][1])
        
        return answer



sol = Solution()

#Test 1
nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3
expected = 12
ans = sol.maxScore(nums1, nums2, k)

if ans == expected:
    print("Test 1 passed")
else:
    print("Test 1 failed")


#Test 2
nums1 = [4,2,3 ,1,1]
nums2 = [7,5,10,9,6]
k = 1
expected = 30
ans = sol.maxScore(nums1, nums2, k)

if ans == expected:
    print("Test 1 passed")
else:
    print("Test 1 failed")


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
