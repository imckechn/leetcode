from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        count = 0
        maxCount = 0
        numLen = len(nums)

        nonOneHit = False

        while right != numLen:
            if nums[right] != 1:
                if nonOneHit:
                    break

                else:
                    nonOneHit = True
            
            else:
                count += 1
            right += 1
        
        maxCount = max(maxCount, count)

        while right != numLen:
            if nums[right] != 1:

                while nums[left] == 1:
                    left += 1
                    count -= 1

                left += 1

            else:
                count += 1
                maxCount = max(maxCount, count)
            
            right += 1

        if not nonOneHit:
            return maxCount-1
        return maxCount

            
sol = Solution()
print(sol.longestSubarray([1,1,1]))