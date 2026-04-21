class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rsplit(None, 1)[-1])

s = Solution()
print(s.lengthOfLastWord("Hello World "))