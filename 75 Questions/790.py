class Solution:
    sequence = [1,2,5]
    
    def numTilings(self, n: int) -> int:
        if n>len(self.sequence):
            self.numTilings(n-1)
            self.sequence.append(self.sequence[n-2]*2 + self.sequence[n-4])
        return self.sequence[n-1]%(10**9 + 7)
            

sol = Solution()
print(sol.numTilings(3))
print(sol.numTilings(4))
print(sol.numTilings(5))