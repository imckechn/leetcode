class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        left = 0
        right = len(s)-1

        while left < right:
            if not s[left].isalpha():
                left += 1
                continue
            elif not s[right].isalpha():
                right -= 1
                continue

            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
    
sol = Solution()
sol.isPalindrome("A man, a plan, a canal: Panama")