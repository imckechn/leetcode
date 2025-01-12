from typing import List, Optional

# Create a graph(s) using the data, search through the graphs (BFS/DFS) and see if you arrive at your start node

class ListNode:
    def __init__(self, val=0, val2=0, next=None):
        self.val = val
        self.val2 = val2
        self.next = [] #arr since there can be multiple children

class Solution:
    def checkForCycle(graph, numCourses, currentLevel):
        if graph.val == graph.val2:
            return True

        currentLevel += 1

        if currentLevel == numCourses:
            return True
        
        else:
            if len(graph.next) > 0:
                for child in graph.next:
                    ans = Solution.checkForCycle(child, numCourses, currentLevel)

                    if ans:
                        return True
                    
        return False

    def checkCourse(elem, graphB, maxDepth):
        if maxDepth == -1:
            return False

        if elem.val == graphB.val2:
            elem.next.append(graphB)
            return True
        else:
            for sub in elem.next:
                ans = Solution.checkCourse(sub, graphB, maxDepth-1)

                if ans:
                    return True
                
            for sub in graphB.next:
                ans = Solution.checkCourse(elem, sub, maxDepth-1)

                if ans:
                    return True

        return False
    
    def addToGraph(graph, course):
        if graph.val2 == course[0]:
            graph.next.append(ListNode(course[0], course[1]))
            return True
        else:
            for sub in graph.next:
                ans = Solution.addToGraph(sub, course)

                if ans:
                    return ans
            return False


    def addCourse(graph, course):   #course needs to be converted to a ListNode before entering this function
        if course[1] == graph.val:
            graph.next.append(ListNode(course[0], course[1]))
            return True
        else:
            newAns = None
            for elem in graph.next:
                newAns = Solution.addToGraph(elem, course)

                if newAns:
                    return True

        return ListNode(course[0], course[1])
    
    def sort(courses):
        if len(courses) < 2:
            return courses

        changed = False

        for i in range(len(courses)-1):
            if courses[0][0] > courses[1][0]:
                temp = courses[0]
                courses[0] = courses[1]
                courses[1] = temp
                changed = True

        if changed:
            return Solution.sort(courses)
        return courses


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites = Solution.sort(prerequisites)
        graphs = []

        for course in prerequisites:
            ans = False
            for graph in graphs:
                ans = Solution.addCourse(graph, course)

                if ans:
                    break
            
            if type(ans) == ListNode:
                graphs.append(ans)

            if not ans:
                graphs.append(ListNode(course[0], course[1]))

        i = 0
        while i < len(graphs):
            for elem in graphs:
                ans = Solution.checkCourse(elem, graphs[i], numCourses)   #Wont work due to graphs[i] being a ListNode
                
                if ans == True and elem != graphs[i]:
                    graphs.pop(i)
            i += 1
        
        for graph in graphs:
            ans = Solution.checkForCycle(graph, numCourses, 0)

            if ans:
                return not ans
            
        return True


# print(Solution.canFinish(None, 2, [[1,0],[0,1]])) #False
# print(Solution.canFinish(None, 2, [[1,0]])) #True
# print(Solution.canFinish(None, 5, [[1,4],[2,4],[3,1],[3,2]])) # True
# print(Solution.canFinish(None, 20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]])) # False
# print(Solution.canFinish(None, 3, [[0,2],[1,2],[2,0]])) # False
# print(Solution.canFinish(None, 4, [[2,0],[1,0],[3,1],[3,2],[1,3]])) # False
print(Solution.canFinish(None, 4, [[0,1],[0,2],[1,3],[3,0]])) # False