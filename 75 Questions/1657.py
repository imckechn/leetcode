from typing import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        if c1.keys() != c2.keys():
            return False
        
        s1 = sorted(c1.values())
        s2 = sorted(c2.values())

        if s1 != s2:
            return False
        return True
    
sol = Solution()
print(sol.closeStrings("abc", "bca"))