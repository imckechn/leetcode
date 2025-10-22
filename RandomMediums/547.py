from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        relationships = {}
        provinces = 0

        for i in range(len(isConnected)):
            r = []
            for j in range(len(isConnected[i])):
                if isConnected[i][j] != 0:
                    r.append(j)

            relationships[i] = r

        #dfs
        for key in relationships.keys():
            if len(relationships[key]) != 0:
                provinceFound = False

                while len(relationships[key]) != 0:
                    elem = relationships[key][0]
                    provinceFound = True

                    relationships[key].remove(elem)
                    if elem == key:
                        continue
                    
                    self.dfs(relationships, elem)

                if provinceFound:
                    provinces += 1

        return provinces


    def dfs(self, rel, index):
        while len(rel[index]) != 0:
            elem = rel[index][0]

            rel[index].remove(elem)
            if elem == index:
                continue
            
            self.dfs(rel, elem)

sol = Solution()

#Test 1
input = [[1,1,0],[1,1,0],[0,0,1]]
expected = 2
ans = sol.findCircleNum(input)

if ans == expected:
    print("Test 1 Passed")
else:
    print("Test 1 Failed")

#Test 2
input = [[1,0,0],[0,1,0],[0,0,1]]
expected = 3
ans = sol.findCircleNum(input)

if ans == expected:
    print("Test 2 Passed")
else:
    print("Test 2 Failed")