class Solution:
    def uniquePaths(self, m: int, n: int) -> int:       
        return Solution.paths(m, n, {"[0,0]":1})

    def paths(m, n, mem):
        if m == 1 or n == 1: return 1

        if str([m,n]) in mem:
            return mem[str([m,n])]

        a = Solution.paths(m-1, n, mem)
        b = Solution.paths(m, n-1, mem)


        if str([m, n]) not in mem.keys():
            mem[str([m, n])] = a + b
            mem[str([n, m])] = a + b
        
        return a+b

print(Solution.uniquePaths(None ,3, 3))
# print(Solution.uniquePaths(None ,3, 2))
# print(Solution.uniquePaths(None ,3, 4))
print(Solution.uniquePaths(None ,3, 7))