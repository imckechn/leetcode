class Solution:
    MIN = 1
    MAX = 26

    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        elif len(s) == 1 and s[0] != "0":
            return 1
        elif s[0] == "0":
            return 0

        if int(s[0]) >= self.MIN and int(s[:2]) <= self.MAX:
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        
        elif int(s[0]) >= self.MIN:
            return self.numDecodings(s[1:])
        
        elif int(s[:2]) <= self.MAX:
            return self.numDecodings(s[2:])

        else:
            return 0
        

sol = Solution()
print(sol.numDecodings("12"))
print(sol.numDecodings("11106"))