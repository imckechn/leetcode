class Solution:
    def climb(n, memo):
        if n in memo:
            return memo[n]
    
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        memo[n] = Solution.climb(n-1, memo) + Solution.climb(n-2, memo)
        return memo[n]

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        #memoization
        memo =  Solution.climb(n-1, {}) + Solution.climb(n-2, {})
        return memo
    

print(Solution.climbStairs(None, 2))
print(Solution.climbStairs(None, 6))