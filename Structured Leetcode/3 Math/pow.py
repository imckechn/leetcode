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

        product = x

        for i in range(n-1):
            product *= x
        
        if isNeg:
            return 1/product
        return product

# print(Solution.myPow(None, 2.1, 3))
print(Solution.myPow(None, 0.00001, 2147483647))
# print(Solution.myPow(None, 8.88023, 3))