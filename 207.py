
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqs = {}
        for course in prerequisites:
            if course[0] in preReqs:
                preReqs[course[0]].append(course[1])
            else:
                preReqs[course[0]] = [course[1]]
        
        while len(preReqs.keys()) != 0:
            ans = self.dfs(preReqs, list(preReqs.keys())[0], [])
            if ans == False:
                return False
        return True
    
    def dfs(self, preReqs, key, visited):
        if key in visited:
            return False
        visited.append(key)

        if key not in preReqs.keys():
            return True
        
        for val in preReqs[key]:
            if val in visited:
                continue
            ans = self.dfs(preReqs, val, visited)
            if not ans:
                return ans
            
        preReqs.pop(key)
        return True

sol = Solution()

numCourses = 2
prerequisites = [[0,1],[0,2],[1,2]]
print("Should be True")
print(sol.canFinish(numCourses, prerequisites))


numCourses = 2
prerequisites = [[1,0],[0,1]]
print("Should be False")
print(sol.canFinish(numCourses, prerequisites))