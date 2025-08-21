class Solution:
    def trailingZeroes(self, n: int) -> int: #not my solution but what a crazy good understanding of math. My math brain needs to be jump started man. smh
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res

print(Solution.trailingZeroes(None, 625))

