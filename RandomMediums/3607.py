from cmath import inf
from typing import List


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        map = {x+1:[] for x in range(c)}
        smallestFound = {x+1:x+1 for x in range(c)}
        disabled = []
        answer = []

        #Create the map
        for connection in connections:
            map[connection[0]].append(connection[1])
            map[connection[1]].append(connection[0])

        #Perform the queries
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

                #See if we've already found the smallest
                if current <= c and smallestFound[current] not in disabled:
                    answer.append(smallestFound[current])
                    continue

                queue = []
                visited = []
                smallest = inf

                while True:
                    if current not in disabled and current < smallest:
                        smallest = current

                    for elem in map[current]:
                        if elem not in visited:
                            queue.append(elem)
                    
                    visited.append(current)

                    if len(queue) == 0:
                        break
                    current = queue.pop(0)

                if smallest == inf:
                    answer.append(-1)
                else:
                    smallestFound[query[1]] = smallest
                    answer.append(smallest)
        return answer




sol = Solution()

# #Test 2
# con = []
# queries = [[1,1],[2,1],[1,1]]
# expected = [1, -1]

# ans = sol.processQueries(3, con, queries)
# if ans != expected:
#     print("Test 2 failed")
# else:
#     print("Test 2 passed")

# #Test 1
# con = [[1,2],[2,3],[3,4],[4,5]]
# queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
# expected = [3,2,3]

# ans = sol.processQueries(5, con, queries)
# if ans != expected:
#     print("Test 1 failed")
# else:
#     print("Test 1 passed")

#Test 3
con = []
queries = [[2,1],[2,1],[1,1],[1,1],[2,1],[1,1],[1,1],[2,1]]
expected = [3,2,3]

ans = sol.processQueries(1, con, queries)
if ans != expected:
    print("Test 3 failed")
else:
    print("Test 3 passed")