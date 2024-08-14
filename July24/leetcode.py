class Solution:
    def lengthOfLongestSubstring(s):
        if len(s) == 0:
            return 0
        elif (len(s) == 1):
            return 1
        
        longestBoi = 1
        currentCount = 1

        i = 0
        j = 1
        lenS = len(s)

        while j != lenS:
            if s[j] in s[i:j]:
                if currentCount > longestBoi:
                    longestBoi = currentCount

                while s[j] in s[i:j]:
                    i += 1

                    if i > j:
                        j = i

                    currentCount = j - i + 1
            else:
                currentCount += 1
            
            j += 1
        
        if currentCount > longestBoi:
            longestBoi = currentCount

        return longestBoi


# print(Solution.lengthOfLongestSubstring("abcabcbb")) #3
# print(Solution.lengthOfLongestSubstring("bbbbb"))
# print(Solution.lengthOfLongestSubstring("pwwkew")) #3
# print(Solution.lengthOfLongestSubstring("dvdf"))
print(Solution.lengthOfLongestSubstring("au"))
# print(Solution.lengthOfLongestSubstring("nfpdmpi"))
