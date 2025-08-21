from typing import List


class Solution:

    def distance(a , b):
        if (a < 0 and b < 0) or (a > 0 and b > 0):
            return a - b
        return a + b
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best = abs(target) - abs(Solution.distance(target, nums[0] + nums[1] + nums[2]))
        values = [nums[0], nums[1], nums[2]]
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
        
            j = i + 1
            k = len(nums) - 1
            while j < k:
                diff = Solution.distance(target, nums[i] + nums[j] + nums[k])
                if  abs(target) - abs(diff) < best:
                    values = [nums[i], nums[j], nums[k]]
                    best =  abs(target) - abs(diff)

                    if best == 0:
                        return sum([x] for x in values)
                    
                else:
                    if diff > 0:
                        k -= 1
                    else: 
                        j += 1
        
        return sum(x for x in values)


print(Solution.threeSumClosest(None, [-1,2,1,-4], 1)) #2
print(Solution.threeSumClosest(None, [1,1,1,0], -100)) #2