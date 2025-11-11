from cmath import inf
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        leftPointer = 0
        rightPointer = len(nums) - 1
        middlePointer = int((rightPointer-leftPointer)/2 + leftPointer)
        closest = nums[0] + nums[1] + nums[2]

        while leftPointer != middlePointer and middlePointer != rightPointer:
            sum = nums[leftPointer] + nums[middlePointer] + nums[rightPointer]

            if abs(target - closest) > abs(target - sum):
                closest = sum

            if sum == target:
                return sum

            elif sum > target:
                if middlePointer-1 > leftPointer:
                    middlePointer -= 1
                
                else:
                    rightPointer -= 1
                    middlePointer = int((rightPointer-leftPointer)/2 + leftPointer)

            else:
                if middlePointer+1 < rightPointer:
                    middlePointer += 1
                
                else:
                    leftPointer += 1
                    middlePointer = int((rightPointer-leftPointer)/2 + leftPointer)

        return sum


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
expected = 3
ans = sol.threeSumClosest(input, -2)

if ans != expected:
    print("T3 Failed")
else:
    print("T3 Passed")