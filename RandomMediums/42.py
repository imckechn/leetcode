class Solution:
    def trap(self, heights) -> int:
        visited = {}
        total = 0

        for j, height in enumerate(heights):
            for i in range(1, height+1):
                if (i in visited):
                    total += j-visited[i]-1
                visited[i] = j

        return total
    

sol = Solution()
sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])