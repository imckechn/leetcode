from math import inf
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        connections = self.createConnectionsMapTwo(routes)

        return self.dfs(connections, routes, [], source, target)
    
    def createConnectionsMapTwo(self, routes):
        map = {}
        for route in routes:
            for i in range(len(route)):
                if i == len(route)-1:
                    if route[i] in map:
                        map[route[i]].append(route[0])
                    else:
                        map[route[i]] = [route[0]]
                else:
                    if route[i] in map:
                        map[route[i]].append(route[i+1])
                    else:
                        map[route[i]] = [route[i+1]]
                    
        return map

    def dfs(self, connections, routes, visited, source, target):     
        while source not in visited:
            if source == target:
                return 1
            
            elif source in visited:
                break

            else:
                visited.append(source)
                if len(connections[source]) > 1:
                    smallest = inf
                    for connection in connections[source]:
                        for route in routes:
                            ans = -1
                            if connection in route and source in route:
                                ans = self.dfs(connections, routes, visited.copy(), connection, target)

                            elif connection in route:
                                ans = self.dfs(connections, routes, visited.copy(), connection, target) + 1

                            if ans != -1:
                                if ans < smallest:
                                    smallest = ans
                    if smallest != inf:
                        return smallest + 1
                    else:
                        return -1
                else: 
                    source = connections[source][0]
        return -1




sol = Solution()

# routes = [[1,2,7],[3,6,7]]
# source = 1
# target = 6

# ans = sol.numBusesToDestination(routes, source, target)
# print(ans)

# routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
# source = 15
# target = 12

# ans = sol.numBusesToDestination(routes, source, target)
# print(ans)

routes = [[25,33],[3,5,13,22,23,29,37,45,49],[15,16,41,47],[5,11,17,23,33],[10,11,12,29,30,39,45],[2,5,23,24,33],[1,2,9,19,20,21,23,32,34,44],[7,18,23,24],[1,2,7,27,36,44],[7,14,33]]
source = 7
target = 42

ans = sol.numBusesToDestination(routes, source, target)
print(ans)
print("SHOULD BE -1")

routes = [[1,9,12,20,23,24,35,38],[10,21,24,31,32,34,37,38,43],[10,19,28,37],[8],[14,19],[11,17,23,31,41,43,44],[21,26,29,33],[5,11,33,41],[4,5,8,9,24,44]]
source = 37
target = 28

ans = sol.numBusesToDestination(routes, source, target)
print(ans)