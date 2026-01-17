from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provinces = []

        def dfs(number):
            found = set()
            for i in range(len(isConnected[number])):
                if isConnected[number][i] != 0:
                    found.add(i)
                    if i not in visited:
                        visited.add(i)
                        found = found.union(dfs(i))

            return found

        for number, connection in enumerate(isConnected):
            if number not in visited:
                visited.add(number)
                provinces.append(dfs(number))
        return len(provinces)
            

sol = Solution()
print(sol.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))