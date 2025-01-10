from typing import List, Optional

# Create a graph(s) using the data, search through the graphs (BFS/DFS) and see if you arrive at your start node

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = [next] #arr since there can be multiple children

class Solution:
    def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
        graphs = []

        for course in prerequisites:
            ans = False
            for graph in graphs:
                ans = Solution.addCourse(graph, course)

                if type(ans) == ListNode:
                    graphs.append(ans)
                    break

                if ans:
                    break

            if not ans:
                graphs.append(ListNode(course[0]))