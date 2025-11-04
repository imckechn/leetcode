from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        stack = [[temperatures[0], 0]]

        for i in range(1, len(temperatures)):            
            answerHeight = len(answer)
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                elem, index = stack.pop(-1)

                if index > answerHeight:
                    answer.insert(answerHeight, i-index)
                else:
                    answer.insert(index, i-index)

            stack.append([temperatures[i], i])
        
        for elem, index in stack:
            answer.insert(index, 0)

        return answer

sol = Solution()

# #Test 1
# temp = [73,74,75,71,69,72,76,73]
# expected = [1,1,4,2,1,1,0,0]
# answer = sol.dailyTemperatures(temp)

# if answer == expected:
#     print("Test 1 passed")
# else:
#     print("Test 1 failed")

# #Test 2
# temp = [30,40,50,60]
# expected = [1,1,1,0]
# answer = sol.dailyTemperatures(temp)

# if answer == expected:
#     print("Test 2 passed")
# else:
#     print("Test 2 failed")

# #Test 3
# temp = [30,60,90]
# expected = [1,1,0]
# answer = sol.dailyTemperatures(temp)

# if answer == expected:
#     print("Test 3 passed")
# else:
#     print("Test 3 failed")

#Test 4
temp = [100,65,67,52,63,40,92,44,66,39]
expected = [0,1,4,1,2,1,0,1,0,0]
answer = sol.dailyTemperatures(temp)

if answer == expected:
    print("Test 4 passed")
else:
    print("Test 4 failed")