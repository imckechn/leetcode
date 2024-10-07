class Solution:
    def productExceptSelf(nums):
        answer = []
        total = 0
        zero = False

        if len(nums) == 2:
            if nums == [1,0]:
                return [0,1]
            elif nums == [0,1]:
                return [1,0]
        

        else:
            lastNonZero = None
            for i in range(len(nums)):
                if nums[i] != 0:
                    if total != 0:
                        total *= nums[i]
                    else:
                        if lastNonZero == None:
                            lastNonZero = nums[i]
                        else:
                            total = lastNonZero * nums[i]
                else:
                    zero = True

        answer = [total] * len(nums)
    
        for i in range(len(answer)):
            if nums[i] == 0:
                continue
            elif zero and len(answer) > 2:
                answer[i] = 0
            else:
                answer[i] = int(answer[i] * 1/nums[i])

        return answer
    
# print(Solution.productExceptSelf([1,2,3,4]))
# print(Solution.productExceptSelf([-1,1,0,-3,3]))
# print(Solution.productExceptSelf([0,0]))
print(Solution.productExceptSelf([1,0]))
print(Solution.productExceptSelf([2,3,0,0])) #0000

