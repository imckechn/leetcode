from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        sequences = {}
        count = 0
                
        #Rows
        for i in range(len(grid)):
            lst = []
            for j in range(len(grid[i])):
                lst.append(grid[i][j])

            try:
                if sequences[str(lst)] != None:
                    sequences[str(lst)] += 1
            except:
                sequences[str(lst)] = 1

        #columns
        for j in range(len(grid[0])):
            lst = []
            for i in range(len(grid)):
                lst.append(grid[i][j])

            try:
                if sequences[str(lst)]:

                    count += sequences[str(lst)]
            except:
                continue

        return count


#Test 1
expected = 1
input = [[3,2,1],[1,7,6],[2,7,7]]
answer = Solution.equalPairs(None, input)
if answer  == expected:
    print("Q1: Passed")

else:
    print("Q1:Failed, expected " + str(expected) + " but got " + str(answer))
            

#Test 2
expected = 3
input = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
answer = Solution.equalPairs(None, input)
if answer  == expected:
    print("Q2: Passed")

else:
    print("Q2:Failed, expected " + str(expected) + " but got " + str(answer))
            