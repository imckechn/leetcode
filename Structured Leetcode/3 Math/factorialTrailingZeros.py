class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        
        zeros = 0
        fact = 1
        for i in range(1, n+1):

            while i%10 == 0:
                zeros += 1
                i //= 10

            fact *= i

            if fact%10 == 0:
                fact //= 10
                zeros += 1

            if fact%10 != 0:
                fact %= 10

        return zeros

print(Solution.trailingZeroes(None, 625))

