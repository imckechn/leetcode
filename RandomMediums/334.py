from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        # Based Case
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] < nums[j]:
        #             for k in range(j+1, len(nums)):
        #                 if nums[j] < nums[k]:
        #                     return True
                        
        # return False

        #Greedy approach
        s = nums[0]
        m = None
        for i in range(1, len(nums)):
            if nums[i] < s and i < len(nums)-2:
                s = nums[i]
                m = None

            else:
                if m == None:
                    m = nums[i]
                else:
                    if nums[i] <= m:
                        m = nums[i]
                    elif s < m and m < nums[i]:
                        return True
            
        return False


# #Test 1
# input = [1,2,3,4,5]
# expected = True
# answer = Solution.increasingTriplet(None, input)

# if (answer == expected):
#     print("Q1: Passed")
# else:
#     print("Q1: Failed, should be " + str(expected))
    

# #Test 2
# input = [5,4,3,2,1]
# expected = False
# answer = Solution.increasingTriplet(None, input)

# if (answer == expected):
#     print("Q2: Passed")
# else:
#     print("Q2: Failed, should be " + str(expected))


# #Test 3
# input = [2,1,5,0,4,6]
# expected = True
# answer = Solution.increasingTriplet(None, input)

# if (answer == expected):
#     print("Q3: Passed")
# else:
#     print("Q3: Failed, should be " + str(expected))


# #Test 4
# input = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# expected = False
# answer = Solution.increasingTriplet(None, input)

# if (answer == expected):
#     print("Q4: Passed")
# else:
#     print("Q4: Failed, should be " + str(expected))


# #Test 5
# input = [5,1,6]
# expected = False
# answer = Solution.increasingTriplet(None, input)

# if (answer == expected):
#     print("Q5: Passed")
# else:
#     print("Q5: Failed, should be " + str(expected))


#Test 6
input = [20,100,10,12,5,13]
expected = True
answer = Solution.increasingTriplet(None, input)

if (answer == expected):
    print("Q6: Passed")
else:
    print("Q6: Failed, should be " + str(expected))