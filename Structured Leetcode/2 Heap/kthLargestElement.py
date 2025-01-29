from typing import List


class Solution:
    def buildMaxHeap(nums):
        heap = [0, nums[0]]

        for i in range(1, len(nums)):
            heap.append(nums[i])
            elemIndex = len(heap)-1

            while True:
                parentIndex = elemIndex // 2

                if elemIndex == 1:
                    break

                elif heap[elemIndex] > heap[parentIndex]:
                    heap[elemIndex], heap[parentIndex] = heap[parentIndex], heap[elemIndex]
                    elemIndex = parentIndex
                else:
                    break

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Solution.buildMaxHeap(nums)

        

Solution.findKthLargest(None, [3,2,1,5,6,4], 3)