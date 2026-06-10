from typing import List


class Solution:
    def dfs(self, courses, course, visited):
        batch = courses[course]
        
        if batch == []:
            return []
        
        for elem in batch:
            if elem in visited and courses[elem] != []:
                return False
    
            else:
                visited.add(elem)
                ans = self.dfs(courses, elem, visited)

                if ans == False:
                    return False
                
        courses[course] = []
        return []

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}
        
        for pair in prerequisites:
            if pair[0] in courses:
                courses[pair[0]].append(pair[1])
                
            else:
                courses[pair[0]] = [pair[1]]

            if pair[1] not in courses:
                    courses[pair[1]] = []

        for key in courses.keys():
            if self.dfs(courses, key, set()) == False:
                return False
            else:
                courses[key] = []
            
        return True
    

            
sol = Solution()
print(sol.canFinish(2, [[1,0]]))
print(sol.canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]))
print(sol.canFinish(3, [[0,1],[0,2],[1,2]]))
print(sol.canFinish(2, [[1,0], [0,1]]))