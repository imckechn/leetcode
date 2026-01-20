class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = []
        matrix.append([1] * n)

        for i in range(m-1):
            matrix.append([1] + [0]*(n-1))

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        return matrix[m-1][n-1]

    
sol = Solution()
print(sol.uniquePaths(3, 7))