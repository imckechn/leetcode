class Solution:
    def uniquePaths(self, m: int, n: int) -> int:       
        return Solution.paths(m, n, {"[0,0]":1})

    def paths(m, n, mem):
        if m == 1 or n == 1: return 1 

        if str([m,n]) in mem:
            return mem[str([m,n])]

        a = Solution.paths(m-1, n, mem)
        if str([m-1, n]) not in mem.keys():
            mem[str([m-1, n])] = a
            mem[str([n, m-1])] = a

        b = Solution.paths(m, n-1, mem)
        if str([m, n-1]) not in mem.keys():
            mem[str([m, n-1])] = a
            mem[str([n-1, m])] = a
        

        return a + b

# print(Solution.uniquePaths(None ,3, 3))
# print(Solution.uniquePaths(None ,3, 2))
print(Solution.uniquePaths(None ,3, 4))
# print(Solution.uniquePaths(None ,3, 7))