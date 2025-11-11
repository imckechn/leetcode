from typing import List

#Do 3sum solution but with 4 fixed variables now
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        length = len(nums)
        for i in range(length-2):
            for j in range(i+1, length-2):
                left = j+1
                right = length-1

                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if sum == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                    
                    elif sum < target:
                        left += 1
                    
                    else:
                        right -= 1

        return [list(x) for x in set(tuple(x) for x in ans)]
    

sol = Solution()

#Test 1
input = [1,0,-1,0,-2,2]
expected = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
ans = sol.fourSum(input, 0)

if ans != expected:
    print("T1 Failed, got " + str(ans))
else:
    print("T1 Passed")