from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        
        par = Solution.generateParenthesis(self, n-1)
        copy = par.copy()

        total = []
        for c in copy:
            total.append("(" + c + ")")

        for p in par:
            total.append("()" + p)

        return total
    
print(Solution.generateParenthesis(None, 1))
print(Solution.generateParenthesis(None, 3))
print(Solution.generateParenthesis(None, 5))