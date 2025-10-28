from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        cost = 0
        first = True
        second = True

        for i in range(k):
            if candidates*2 < len(costs):
                can1 = costs[:candidates]
                mid = costs[candidates:len(costs)-candidates]
                can2 = costs[len(costs)-candidates:]

                can1.sort()
                can2.sort()

                if can1[0] <= can2[0]:
                    cost += can1.pop(0)
                else:
                    cost += can2.pop(0)

                costs = can1 + mid + can2

            else:
                costs.sort()
                cost += costs.pop(0)

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