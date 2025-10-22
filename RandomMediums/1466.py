from typing import List, Tuple


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # pointingToZero = {0: True}
        # count = 0

        # while len(pointingToZero.keys()) != n:
        #     for con in connections:
        #         if con[0] in pointingToZero.keys() and con[1] not in pointingToZero.keys():
        #             con[1], con[0] = con[0], con[1]
        #             pointingToZero[con[0]] = True
        #             count += 1

        #         elif con[1] in pointingToZero.keys():
        #             pointingToZero[con[0]] = True

        # return count
    

        #Better Soln
        adj = [[] for _ in range(n)]
        for connection in connections:
            adj[connection[0]].append((connection[1], 1))
            adj[connection[1]].append((connection[0], -1))
        visited = [False] * n
        minChange = [0]
        self.dfs(adj, visited, minChange, 0)
        return minChange[0]
    
    def dfs(self, adj: List[List[Tuple[int, int]]], visited: List[bool], minChange: List[int], currCity: int) -> None:
            visited[currCity] = True
            for neighbourCity in adj[currCity]:
                if not visited[neighbourCity[0]]:
                    if neighbourCity[1] == 1:
                        minChange[0] += 1
                    self.dfs(adj, visited, minChange, neighbourCity[0])
    
sol = Solution()

#Test 1
input = [[0,1],[1,3],[2,3],[4,0],[4,5]]
expected = 3
ans = sol.minReorder(6, input)

if ans == expected:
    print("Test 1 passed")
else:
    print("Test 1 Failed")

#Test 2
input = [[1,0],[1,2],[3,2],[3,4]]
expected = 2
ans = sol.minReorder(5, input)

if ans == expected:
    print("Test 2 passed")
else:
    print("Test 2 Failed")

#Test 3
input = [[4,5],[0,1],[1,3],[2,3],[4,0]]
expected = 3
ans = sol.minReorder(6, input)

if ans == expected:
    print("Test 3 passed")
else:
    print("Test 3 Failed")