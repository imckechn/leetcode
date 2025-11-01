from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans =  self.comboSum([1,2,3,4,5,6,7,8,9], n , k, [])

        unique_sublists = []
        seen = set()
        for sub in ans:
            if len(sub) == len(set(sub)):  # all elements unique
                key = tuple(sorted(sub))
                if key not in seen:
                    seen.add(key)
                    unique_sublists.append(sub)

        return unique_sublists

    def comboSum(self, numSet: list[int], target: int, choicesLeft: int, currentChoices: list[int]):
        if choicesLeft == 0:
            return
        
        if choicesLeft == 1:
            finalOption = target - sum(currentChoices)

            if finalOption in numSet:
                currentChoices.append(finalOption)
                return [currentChoices]
            else:
                return None
            
        else:
            answers = []
            for i in range(len(numSet)):
                ans = self.comboSum(numSet[:i] + numSet[i+1:], target, choicesLeft-1, currentChoices + [numSet[i]])

                if ans != None:
                    answers = answers + ans

            return answers
        

sol = Solution()

#Test 1
k = 3
n = 7
expected = [[1,2,4]]
answer = sol.combinationSum3(k, n)

if answer == expected:
    print("Test 1 passed")
else:
    print("Test 1 failed")


#Test 2
k = 3
n = 9
expected = [[1,2,6],[1,3,5],[2,3,4]]
answer = sol.combinationSum3(k, n)

if answer == expected:
    print("Test 2 passed")
else:
    print("Test 2 failed")

