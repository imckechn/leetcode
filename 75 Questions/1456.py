class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        maxCount = 0
        currentCount = 0

        for i in range(k):
            if i >= len(s):
                return maxCount
            
            if s[i] in vowels:
                currentCount += 1

        maxCount = max(currentCount, maxCount)

        for i in range(len(s)-k):
            if maxCount == k:
                break

            if s[i] in vowels and currentCount > 0:
                currentCount-=1

            if s[i+k] in vowels:
                currentCount += 1
                
            maxCount = max(currentCount, maxCount)

        return maxCount

                
    
sol = Solution()
print(sol.maxVowels("tryhard", 4)) #1
print(sol.maxVowels("tnfazcwrryitgacaabwm", 4)) #3
print(sol.maxVowels("weallloveyou", 7)) #4
print(sol.maxVowels("abciiidef", 3)) #3
print(sol.maxVowels("leetcode", 3)) #2