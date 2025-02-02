class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        if n == 0:
            return 1
        
        isNeg = False
        if n < 0:
            n *= -1
            isNeg = True

        if n % 2 == 0:
            half = Solution.myPow(self, x, n // 2)
            ans = half * half
        else:
            ans = x * Solution.myPow(self, x, n-1)

        if isNeg:
            return 1/ans
        return ans


print(Solution.myPow(None, 2, -2))
print(Solution.myPow(None, 2.1, 3))
print(Solution.myPow(None, 0.00001, 2147483647))
print(Solution.myPow(None, 8.88023, 3))