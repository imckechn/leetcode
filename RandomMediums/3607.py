from cmath import inf
from typing import List


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        map = {x+1:[] for x in range(c)}
        disabled = []
        answer = []

        #Create the map
        for connection in connections:
            map[connection[0]].append(connection[1])
            map[connection[1]].append(connection[0])

        #Create the groups
        groups = []
        for node in map:
            groupExists = False
            for i in range(len(groups)):
            # for group in groups:
                if node in groups[i]:
                    groupExists = True
                    temp = set(map[node])
                    temp.add(node)
                    groups[i] = groups[i].union(temp)
                    break

                else:
                    for child in map[node]:
                        if child in groups[i]:
                            groupExists = True
                            temp = set(map[node])
                            temp.add(node)
                            groups[i] = groups[i].union(temp)
                            break
                
            if not groupExists:
                temp = set(map[node])
                temp.add(node)
                groups.append(temp)

        #Turn the groups into lists and sort by ascending
        sortedGroups = []
        for group in groups:
            g = list(group)
            g.sort()
            sortedGroups.append(g)

        # #Perform the queries
        for query in queries:
            
            #Disabled
            if query[0] == 2:
                disabled.append(query[1])
                continue
            
            #Health check
            if query[1] not in disabled:
                answer.append(query[1])

            else:
                current = query[1]

                notFound = True
                for group in sortedGroups:
                    if current in group:
                        for elem in group:
                            if elem not in disabled:
                                notFound = False
                                answer.append(elem)
                                break
                        break

                if notFound:
                    answer.append(-1)
        return answer




sol = Solution()

#Test 1
con = [[1,2],[2,3],[3,4],[4,5]]
queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
expected = [3,2,3]

ans = sol.processQueries(5, con, queries)
if ans != expected:
    print("Test 1 failed")
else:
    print("Test 1 passed")

#Test 2
con = []
queries = [[1,1],[2,1],[1,1]]
expected = [1, -1]

ans = sol.processQueries(3, con, queries)
if ans != expected:
    print("Test 2 failed")
else:
    print("Test 2 passed")

#Test 3
con = []
queries = [[2,1],[2,1],[1,1],[1,1],[2,1],[1,1],[1,1],[2,1]]
expected = [3,2,3]

ans = sol.processQueries(1, con, queries)
if ans != expected:
    print("Test 3 failed, got " + str(ans))
else:
    print("Test 3 passed")