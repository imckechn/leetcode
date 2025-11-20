from math import inf
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        visitedStops = []
        visitedRoutes = []

        connections = self.createConnectionsMap(routes)
        return self.dfs(connections, visitedStops, visitedRoutes, source, target)

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
        if target == source:
            return len(visitedRoutes) + 1
        elif source in visitedStops:
            return -1
        
        visitedStops.append(source)       

        smallest = inf
        for route in connections[source]:
            if route in visitedRoutes:
                continue

            for stop in route:
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


# for i in range(len(route)):
                # if i == len(route)-1:
                #     if route[i] in ans:
                #         ans[route[i]].append(route[0])
                #     else:
                #         ans[route[i]] = [route[0]]

                # else:
                #     if route[i] in ans:
                #         ans[route[i]].append(route[i+1])
                #     else:
                #         ans[route[i]] = [route[i+1]]