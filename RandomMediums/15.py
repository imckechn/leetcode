from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if j == i:
                    continue

                for k in range(j+1, len(nums)):
                    if k == j:
                        continue
                    else:
                        if nums[i] + nums[j] + nums[k] == 0 and [nums[i],nums[j],nums[k]] not in triplets:
                            triplets.append([nums[i],nums[j],nums[k]])
        
        return triplets
    

print(Solution.threeSum(None, [-1,0,1,2,-1,-4]))