from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool: #Should be able to take a greedy approach to jumping
        path = [nums[0]]
        jump = [nums[0]]
        currentIndex = [0]

        while currentIndex[-1] + jump[-1] < len(nums):  #Getting an error where my jump is 0
            if jump[-1] == 0:
                    jump.pop()
                    currentIndex.pop()
                    path.pop()
                    jump[-1] -= 1

                    if path == []:
                        return False
                    continue

            if nums[currentIndex[-1] + jump[-1]] != 0:
                path.append(nums[currentIndex[-1] + jump[-1]])
                currentIndex.append(nums[jump[-1]])
                jump.append(nums[currentIndex[-1] + jump[-1]])

            else:
                jump[-1] -= 1

                
        
        return True
                    
# print(Solution.canJump(None,  [2,3,1,1,4])) #True
print(Solution.canJump(None,  [3,2,1,0,4])) #True
