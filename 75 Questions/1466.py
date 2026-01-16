from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = {}
        swaps = 0

        for i in range(n):
            roads[i] = []

        for connection in connections:
            roads[connection[0]].append(connection[1])
        
        while True:
            for key, values in roads.items():
                if 0 in values:
                    newValues = roads[key]
                    roads[key] = []
                    newValues.remove(0)
                    roads[0] += newValues

            newVals = []
            for value in roads[0]:
                swaps += 1

                if value in roads:
                    newVals += roads[value]
                    roads[value] = []

            roads[0] = newVals

            if roads[0] != []:
                break

        return swaps

    
sol = Solution()
sol.minReorder(5, [[1,0],[1,2],[3,2],[3,4]])
sol.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]])

        