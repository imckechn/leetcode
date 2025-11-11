from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.addParenth("(", n-1, n)
        
    def addParenth(self, combo, open, closed):
        if open <= 0 and closed <= 0:
            return [combo]
        
        ans = []
        if open > 0:
            ans += self.addParenth(combo + "(", open-1, closed)

        if closed > 0 and open < closed:
            ans += self.addParenth(combo + ")", open, closed-1)
        return ans


sol = Solution()

#Test 1
n = 3
expected = ["((()))","(()())","(())()","()(())","()()()"]
ans = sol.generateParenthesis(n)
if ans != expected:
    print("T1 Failed, got " + str(ans))
else:
    print("T1 Success")


#Test 2
n = 1
expected = ["()"]
ans = sol.generateParenthesis(n)
if ans != expected:
    print("T2 Failed")
else:
    print("T2 Success")