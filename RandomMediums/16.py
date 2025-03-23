from typing import List


class Solution:

    def distance(a , b):
        if (a < 0 and b < 0) or (a > 0 and b > 0):
            return a - b
        return a + b
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best = abs(target) - abs((nums[0] + nums[1] + nums[2]))
        values = [nums[0], nums[1], nums[2]]

        positives = []
        negatives = []
        zeros = 0

        for num in nums:
            if num < 0:
                negatives.append(num)
            elif num > 0:
                positives.append(num)
            else:
                zeros += 1

        if zeros > 1:
            for pos in positives:
                for neg in negatives:
                    if target == pos + neg:
                        return target

                    if abs(Solution.distance(target, pos + neg)) < best:
                        best = abs(pos + neg)
                        values = [pos, neg, 0]

        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == target:
                    return target
                
                elif abs(Solution.distance(target, (nums[i] + nums[left] + nums[right]))) < best:
                    best = abs(nums[i] + nums[left] + nums[right])
                    values = [nums[i], nums[left], nums[right]]
                    left += 1

                else:
                    if nums[i] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1

        return sum(val for val in values)


# print(Solution.threeSumClosest(None, [-1,2,1,-4], 1)) #2
print(Solution.threeSumClosest(None, [1,1,1,0], -100)) #2