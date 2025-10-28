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

                if first:
                    can1.sort()
                    can2.sort()
                    first = False

                if can1[0] <= can2[0]:
                    cost += can1.pop(0)
                    new = mid.pop(0)
                    for i in range(len(can1)):
                        if can1[i] > new:
                            can1.insert(i, new)
                            new = -1
                            break
                    
                    if new != -1:
                        can1.append(new)
                    
                else:
                    cost += can2.pop(0)
                    new = mid.pop()
                    for i in range(len(can2)):
                        if can2[i] > new:
                            can2.insert(i, new)
                            new = -1
                            break

                    if new != -1:
                        can2.append(new)

                costs = can1 + mid + can2

            else:
                if second:
                    costs.sort()
                    second = False
                cost += costs.pop(0)

        return cost

sol = Solution()

# #Test 1
# costs = [17,12,10,2,7,2,11,20,8]
# k = 3
# can = 4
# expected = 11

# ans = sol.totalCost(costs, k, can)
# if ans == expected:
#     print("Test 1 passed")
# else:
#     print("Test 2 failed")


# #Test 2
# costs = [1,2,4,1]
# k = 3
# can = 3
# expected = 4

# ans = sol.totalCost(costs, k, can)
# if ans == expected:
#     print("Test 2 passed")
# else:
#     print("Test 2 failed")


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