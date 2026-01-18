import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        leftHeap = []
        rightHeap = []

        lp = 0
        rp = len(costs)-1

        #populateHeap
        for i in range(candidates):
            if lp == rp:
                heapq.heappush(leftHeap, costs[lp])
                lp += 1
                break

            elif lp > rp:
                break

            else:
                heapq.heappush(leftHeap, costs[lp])
                lp += 1

                heapq.heappush(rightHeap, costs[rp])
                rp  -= 1

        #pop candidates number off heap
        sum = 0
        for i in range(k):
            if len(leftHeap) == 0:
                sum += heapq.heappop(rightHeap)
            elif len(rightHeap) == 0:
                sum += heapq.heappop(leftHeap)

            elif leftHeap[0] <= rightHeap[0]:
                sum += heapq.heappop(leftHeap)

                if lp <= rp:
                    heapq.heappush(leftHeap, costs[lp])
                    lp += 1
            
            else:
                sum += heapq.heappop(rightHeap)
                if lp <= rp:
                    heapq.heappush(rightHeap, costs[rp])
                    rp -= 1
        return sum
    
sol = Solution()
sol.totalCost([17,12,10,2,7,2,11,20,8], 3, 4)