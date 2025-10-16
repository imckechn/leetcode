from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #Possible solution 1
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                count += 1
            else:
                i += 1

        for i in range(count):
            nums.append(0) 

        #Possible solution 2
        # end = len(nums) - 1
        # start = 0

        # while start != end:
        #     if nums[start] == 0:
        #         nums.pop(start)
        #         nums.insert(end, 0)
        #         end -= 1
        #     else:
        #         start += 1
    
        return nums

        
if Solution.moveZeroes(None, [0,1,0,3,12]) == [1,3,12,0,0]:
    print("Test 1 passed")
else:
    print("Failed")

    

        
if Solution.moveZeroes(None, [0]) == [0]:
    print("Test 2 passed")
else:
    print("Failed")

    