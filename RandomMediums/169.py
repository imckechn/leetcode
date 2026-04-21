class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        counts = {}
        largest = 1
        val = nums[0]

        for num in nums:
            if num in counts:
                counts[num] += 1
                
                if counts[num] > largest:
                    val = num
                    largest = counts[num]

            else:
                counts[num] = 1
        
        return val

sol = Solution()
print(sol.majorityElement([3,2,3]))
print(sol.majorityElement([2,2,1,1,1,2,2]))