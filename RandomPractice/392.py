class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPointer = 0
        tPointer = 0

        while tPointer < len(t):
            if sPointer == len(s):
                return True
            
            if s[sPointer] == t[tPointer]:
                sPointer += 1

            tPointer += 1
        
        if sPointer == len(s):
            return True
        
        return False
    
sol = Solution()
sol.isSubsequence("abc", "ahbgdc")