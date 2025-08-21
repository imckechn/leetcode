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
        return heap
    
    def restoreHeap(heap):
        curIndex = 1
        while True:
            if curIndex*2+1 >= len(heap):
                if curIndex*2 < len(heap) and heap[curIndex] < heap[curIndex*2]:
                    heap[curIndex],  heap[curIndex*2] =  heap[curIndex*2], heap[curIndex]
                        
                return heap

            largestIndex = curIndex*2 if heap[curIndex*2] > heap[curIndex*2 + 1] else curIndex*2 + 1
            if heap[curIndex] < heap[largestIndex]:
                heap[curIndex],  heap[largestIndex] =  heap[largestIndex], heap[curIndex]
                curIndex = largestIndex
            else:
                return heap
        

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Solution.buildMaxHeap(nums)
        
        largest = 0
        for i in range(k):
            if len(heap) == 2:
                return heap[1]
        
            largest, heap[1] = heap[1], heap.pop(-1)
            heap = Solution.restoreHeap(heap)

        return largest



# print(Solution.findKthLargest(None, [3,2,1,5,6,4], 3))
# print(Solution.findKthLargest(None, [3,2,3,1,2,4,5,5,6], 4))
print(Solution.findKthLargest(None, [3,2,3,1,2,4,5,5,6], 9))