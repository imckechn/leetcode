from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        cost = 0
        larger = False
        
        if candidates*2 < len(costs):
            larger = True
            can1 = costs[:candidates]
            mid = costs[candidates:len(costs)-candidates]
            can2 = costs[len(costs)-candidates:]
            heapify(can1)
            heapify(can2)

            while k > 0 and len(mid) > 0:
                k -= 1
                if can1[0] <= can2[0]:
                    cost += heappop(can1)
                    heappush(can1, mid.pop(0))
                    
                else:
                    cost += heappop(can2)
                    heappush(can2, mid.pop())
        
        if larger:
            costs = can1 + can2

        heapify(costs)

        while k > 0 and costs != []:
            k -= 1
            cost += heappop(costs)

        return cost


sol = Solution()

#Test 1
costs = [17,12,10,2,7,2,11,20,8]
k = 3
can = 4
expected = 11

ans = sol.totalCost(costs, k, can)
if ans == expected:
    print("Test 1 passed")
else:
    print("Test 2 failed")


#Test 2
costs = [1,2,4,1]
k = 3
can = 3
expected = 4

ans = sol.totalCost(costs, k, can)
if ans == expected:
    print("Test 2 passed")
else:
    print("Test 2 failed")


#Test 3
costs = [31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58]
k = 11
can = 2
expected = 423

ans = sol.totalCost(costs, k, can)
if ans == expected:
    print("Test 3 passed")
else:
    print("Test 3 failed")