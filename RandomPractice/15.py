class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        a = 0
        answer = []
        
        while a < len(nums) - 2:
            b = a+1
            c = len(nums)-1

            while b < c:
                total = nums[a] + nums[b] + nums[c]
                
                if total == 0:
                    if [nums[a], nums[b], nums[c]] not in answer:
                        answer.append([nums[a], nums[b], nums[c]])
                    b += 1

                elif total < 0:
                    b += 1
                    while b < len(nums)-1 and nums[b-1] == nums[b]:
                        b += 1

                else:
                    c -= 1
                    while c >= 0 and nums[c] == nums[c+1]:
                        c -= 1

            a += 1
            while a < len(nums)-1 and nums[a-1] == nums[a]:
                a += 1
        
        return answer
    
sol = Solution()
# print(sol.threeSum([0,0,0]))
print(sol.threeSum([1,2,0,1,0,0,0,0]))
# print(sol.threeSum([-1,0,1,2,-1,-4]))