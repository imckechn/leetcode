from math import inf
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        connections = self.createConnectionsMap(routes)
        return self.dfs(connections, [], [], source, target)

    def createConnectionsMap(self, routes):
        ans = {}

        for route in routes:
            for stop in route:
                if stop in ans:
                    ans[stop].append(route)
                else:
                    ans[stop] = [route]
        return ans
    
    def dfs(self, connections, visitedStops, visitedRoutes, source, target):        
        visitedStops.append(source)

        smallest = inf
        for route in connections[source]:
            if route in visitedRoutes:
                continue

            elif target in route:
                return len(visitedRoutes) + 1

            for stop in route:
                if stop in visitedStops or stop == source:
                    continue

                if len(connections[stop]) > 1:
                    ans = self.dfs(connections, visitedStops.copy(), visitedRoutes.copy(), stop, target)
                    if ans != -1 and ans < smallest:
                        smallest = ans

            visitedRoutes.append(route)

        if smallest == inf:
            return -1
        else:
            return smallest



sol = Solution()

routes = [[1,2,7],[3,6,7]]
source = 1
target = 6

ans = sol.numBusesToDestination(routes, source, target)
print(ans)

routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
source = 15
target = 12

ans = sol.numBusesToDestination(routes, source, target)
print(ans)

routes = [[25,33],[3,5,13,22,23,29,37,45,49],[15,16,41,47],[5,11,17,23,33],[10,11,12,29,30,39,45],[2,5,23,24,33],[1,2,9,19,20,21,23,32,34,44],[7,18,23,24],[1,2,7,27,36,44],[7,14,33]]
source = 7
target = 42

ans = sol.numBusesToDestination(routes, source, target)
print(ans)

routes = [[1,9,12,20,23,24,35,38],[10,21,24,31,32,34,37,38,43],[10,19,28,37],[8],[14,19],[11,17,23,31,41,43,44],[21,26,29,33],[5,11,33,41],[4,5,8,9,24,44]]
source = 37
target = 28

ans = sol.numBusesToDestination(routes, source, target)
print(ans)