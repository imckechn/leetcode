class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()

        left = 0
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1

        return True

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))