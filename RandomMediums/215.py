from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Solution.heapify(nums)[k-1]

        return Solution.popOffHeap(k)[0]
    

    def popOffHeap(k):
        
    


    #Create the max heap
    def heapify(nums):
        heap = []

        for num in nums:
            heap.append(num)

            index = len(heap) - 1
            while heap[index] > heap[int(index/2)]:
                heap[index], heap[int(index/2)] = heap[int(index/2)], heap[index]
                index = int(index/2)

        return heap


sol = Solution()

# #Test 1
# input = [3,2,1,5,6,4]
# k = 2
# expected = 5
# ans = sol.findKthLargest(input, k)
# if ans == expected:
#     print("Test 1 passed")
# else:
#     print("Test 1 failed")


# #Test 2
# input = [3,2,3,1,2,4,5,5,6]
# k = 4
# expected = 4
# ans = sol.findKthLargest(input, k)
# if ans == expected:
#     print("Test 2 passed")
# else:
#     print("Test 2 failed")


#Test 3
input = [5,2,4,1,3,6,0]
k = 4
expected = 3
ans = sol.findKthLargest(input, k)
if ans == expected:
    print("Test 3 passed")
else:
    print("Test 3 failed")