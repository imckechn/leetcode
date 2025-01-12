from typing import List, Optional

# Create a graph(s) using the data, search through the graphs (BFS/DFS) and see if you arrive at your start node

class ListNode:
    def __init__(self, val=0, val2=0, next=None):
        self.val = val
        self.val2 = val2
        self.next = [] #arr since there can be multiple children

class Solution:
    def checkForCycle(graph, numCourses, currentLevel):
        currentLevel += 1

        if currentLevel == numCourses:
            return False
        
        else:
            if len(graph.next) > 0:
                for child in graph.next:
                    ans = Solution.checkForCycle(child, numCourses, currentLevel)

                    if not ans:
                        return False
                    
        return True

    def checkCourse(graphA, graphB):
        if graphA.val2 == graphB.val:
            graphA.next.append(graphB)
            return True
        else:
            ans = None
            for elem in graphA.next:
                newAns = Solution.checkCourse(elem, graphB)

                if newAns:
                    return True

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
                graphs.append(ListNode(course[0], course[1]))

        #See if you can reorg the graph to attach them to eachother

        i = 0
        while i < len(graphs):
            for elem in graphs:
                ans = Solution.checkCourse(elem, graphs[i])   #Wont work due to graphs[i] being a ListNode
                
                if ans == True and elem != graphs[i]:
                    graphs.pop(i)
                else:
                    i += 1
        
        for graph in graphs:
            ans = Solution.checkForCycle(graph, numCourses, 0)

            if not ans:
                return ans
            
        return True


print(Solution.canFinish(2, [[1,0],[0,1]]))