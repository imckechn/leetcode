class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        left = 0
        right = 0
        maxCount = 0
        currentCount = 0

        for i in range(k):
            if right >= len(s):
                return maxCount
            
            if s[right] in vowels:
                currentCount += 1
            right += 1
        
        right -= 1
        maxCount = max(maxCount, currentCount)

        while right < len(s):
            if s[left] in vowels:
                currentCount -= 1
            left += 1

            right += 1
            if right < len(s) and s[right] in vowels:
                currentCount += 1
            maxCount = max(maxCount, currentCount)

        return maxCount

                
    
sol = Solution()
print(sol.maxVowels("abciiidef", 3))
print(sol.maxVowels("leetcode", 3))