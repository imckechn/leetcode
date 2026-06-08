class Solution:
    def climb(self, n, values):
        if n in values.keys():
            return values
        else:
            if (n >= 2):
                values = self.climb(n-1, values)
                values = self.climb(n-2, values)
                values[n] = values[n-1] + values[n-2]
            return values

    def climbStairs(self, n: int) -> int:
        values = self.climb(n, {0:0, 1:1, 2:2})
        return values[n]
    
sol = Solution()
print(sol.climbStairs(44))