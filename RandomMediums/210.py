from typing import List

class Node:
    def __init__(self, value, prereq):
        self.val = value

        if prereq != None:
            self.children = [prereq]
        else:
            self.children = []

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]

        prerequisites.sort()

        first = prerequisites.pop(0)

        child = Node(first[0], None)
        head = Node(first[1], child)

        preerqs = {}
        preerqs[first[1]] = head
        preerqs[first[0]] = child

        for course in prerequisites:
            if course[0] not in preerqs:
                newChild = Node(course[0], None)
                preerqs[course[1]].children.append(newChild)
                preerqs[course[0]] = newChild
            
            else:
                if course[1] in preerqs and preerqs[course[1]] in preerqs[course[0]].children:
                    return []
                else:
                    preerqs[course[1]].children.append(preerqs[course[0]])


        output = []
        found = set()
        queue = [head]

        while queue != []:
            val = queue.pop(0)

            if val.val not in found:
                output.append(val.val)
                found.add(val.val)
            queue += val.children

        if len(output) < numCourses:
            for i in range(numCourses):
                if i not in output:
                    output.append(i)

        return output

sol = Solution()
print(sol.findOrder(3, [[2,0],[2,1]]))
print(sol.findOrder(2, [[0,1],[1,0]]))
print(sol.findOrder(2, [[0,1]]))

print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))


