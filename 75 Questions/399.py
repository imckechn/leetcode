from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        map = {}
        validLetters = set()

        for i in range(len(equations)):
            map[equations[i][0]] = []
            map[equations[i][1]] = []

        for i in range(len(equations)):
            map[equations[i][0]].append([equations[i][1], values[i]])
            map[equations[i][1]].append([equations[i][0], (1/values[i])])
            validLetters.add(equations[i][0])
            validLetters.add(equations[i][1])
            
        def dfs(start, stop):
            if start in visited:
                return -1
            
            elif start == stop:
                return 1
            
            visited.add(start)

            for path in map[start]:
                ans = dfs(path[0], stop)
                if ans != -1:
                    return ans * path[1]
                
            return -1

        answers = []
        for query in queries:
            visited = set()

            if query[0] not in validLetters or query[1] not in validLetters:
                answers.append(-1)

            elif query[0] == query[1]:
                answers.append(1)

            else:
                answers.append(dfs(query[0], query[1]))
        return answers

sol = Solution()
print(sol.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
