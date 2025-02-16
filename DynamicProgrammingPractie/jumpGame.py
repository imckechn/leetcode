from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool: #Should be able to take a greedy approach to jumping
        path = [nums[0]]
        jump = [nums[0]]
        currentIndex = [0]

        while currentIndex[-1] + jump[-1] < len(nums) and currentIndex[-1] != len(nums) -1:  #Getting an error where my jump is 0
            if jump[-1] == 0:
                    jump.pop()
                    currentIndex.pop()
                    path.pop()

                    if path == []:
                        return False
            
                    jump[-1] -= 1
                    continue

            path.append(nums[currentIndex[-1] + jump[-1]])
            currentIndex.append(currentIndex[-1] + jump[-1])
            jump.append(nums[currentIndex[-1]])

        return True
                    
print(Solution.canJump(None,  [2,3,1,1,4])) #True
print(Solution.canJump(None,  [3,2,1,0,4])) #False
print(Solution.canJump(None,  [2,0,0])) #True
