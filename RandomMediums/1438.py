from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        numsLength = len(nums)
        if numsLength <= 1:
            return numsLength
        
        count = 1
        left = 0
        right = 1
        smallest = min(nums[left], nums[right])
        largest = max(nums[left], nums[right])

        while right < numsLength:

            #Expand window to the right
            if largest - smallest <= limit:
                right += 1

                if right-left > count:
                    count = (right - left)

                if right == numsLength:
                    break

                smallest = min(smallest, nums[right])
                largest =  max(largest, nums[right])

            #reduce window size from right 
            #Make sure left != right
            else:
                if left == numsLength:
                    break

                if nums[left] == smallest:
                    newSmallest = nums[left+1]
                    index = left+1
                    for i in range(left+1, right):
                        if nums[i] < newSmallest:
                            newSmallest = nums[i]
                            index = i

                    left = index
                    smallest = newSmallest


                elif nums[left] == largest:
                    newLargest = nums[left+1]
                    index = left+1
                    for i in range(left+1, right):
                        if nums[i] > newLargest:
                            newLargest = nums[i]
                            index = i

                    left = index
                    largest = newLargest

                else:
                    left += 1
        return count
    
sol = Solution()

ans =  sol.longestSubarray([8,2,4,7], 4)
if ans != 2:
    print("Failed got " + str(ans))
else:
    print("Passed")

ans =  sol.longestSubarray([10,1,2,4,7,2], 5)
if ans != 4:
    print("Failed got " + str(ans))
else:
    print("Passed")

ans =  sol.longestSubarray([4,2,2,2,4,4,2,2], 0)
if ans != 3:
    print("Failed got " + str(ans))
else:
    print("Passed")

