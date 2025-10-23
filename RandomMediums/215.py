from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heap.insert(0, num)
            Solution.heapify_down(heap)

        for i in range(k-1):
            heap[0] = heap.pop()
            Solution.heapify_down(heap)

        return heap[0]

    def heapify_down(heap, index=0):
        size = len(heap)
        smallest = index

        left = 2 * index + 1
        right = 2 * index + 2

        # Check if right child is larger
        if right < size and heap[right] > heap[smallest]:
            smallest = right

        # Check if left child is larger
        if left < size and heap[left] > heap[smallest]:
            smallest = left

        # If a child is smaller, swap and continue recursively
        if smallest != index:
            heap[index], heap[smallest] = heap[smallest], heap[index]
            Solution.heapify_down(heap, smallest)

sol = Solution()

#Test 1
input = [3,2,1,5,6,4]
k = 2
expected = 5
ans = sol.findKthLargest(input, k)
if ans == expected:
    print("Test 1 passed")
else:
    print("Test 1 failed")


#Test 2
input = [3,2,3,1,2,4,5,5,-6]
k = 4
expected = 3
ans = sol.findKthLargest(input, k)
if ans == expected:
    print("Test 2 passed")
else:
    print("Test 2 failed")


#Test 3
input = [5,2,4,1,3,6,0]
k = 4
expected = 3
ans = sol.findKthLargest(input, k)
if ans == expected:
    print("Test 3 passed")
else:
    print("Test 3 failed")