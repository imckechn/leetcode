class Solution:
    sequence = [0,1,1]

    def tribonacci(self, n: int) -> int:
        if n >= len(self.sequence):
            for i in range(len(self.sequence)-1, n+1):
                self.sequence.append(self.sequence[-1] + self.sequence[-2] + self.sequence[-3])
        return self.sequence[n]

sol = Solution()
print(sol.tribonacci(4))
print(sol.tribonacci(10))
print(sol.tribonacci(100))