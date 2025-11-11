from cmath import inf
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = inf

        for fixed in range(len(nums)-1):
            left = fixed+1
            right = len(nums)-1

            while left != right:
                sum = nums[fixed] + nums[left] + nums[right]

                if abs(target-sum) < abs(target-closest):
                    closest = sum

                if sum > target:
                    right -=1
                else:
                    left += 1
            
        return closest


sol = Solution()

# #Test 1
# input = [-1,2,1,-4]
# expected = 2
# ans = sol.threeSumClosest(input, 1)

# if ans != expected:
#     print("T1 Failed")
# else:
#     print("T1 Passed")

# #Test 2
# input = [0,0,0]
# expected = 0
# ans = sol.threeSumClosest(input, 2)

# if ans != expected:
#     print("T2 Failed")
# else:
#     print("T2 Passed")

#Test 3
input = [4,0,5,-5,3,3,0,-4,-5]
expected = -2
ans = sol.threeSumClosest(input, -2)

if ans != expected:
    print("T3 Failed, got " + str(ans))
else:
    print("T3 Passed")