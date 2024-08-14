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
                currentCount = 0
            else:
                currentCount += 1
            
            j += 1

        return longestBoi


        
        
        
        if len(s) == 0:
            return 0
        elif (len(s) == 1):
            return 1
        
        longestSubstringLength = 0
        j = 0
        strLen = len(s)

        for i in range(strLen-1):
            for j in range(i+1, strLen):
                if s[j] in s[i:j]:
                    if j-i > longestSubstringLength:
                        longestSubstringLength = j-i

                        i = s[i:j].index(s[j])
                    break
                
                if j + 1 == strLen:
                    if j-i + 1 > longestSubstringLength:
                        longestSubstringLength = j-i + 1
                    break
            
            if j == strLen - 1:
                break
        
        return longestSubstringLength



        

print(Solution.lengthOfLongestSubstring("abcabcbb"))
# print(Solution.lengthOfLongestSubstring("bbbbb"))
# print(Solution.lengthOfLongestSubstring("pwwkew"))
print(Solution.lengthOfLongestSubstring("au"))
print(Solution.lengthOfLongestSubstring("nfpdmpi"))



#Go through the string, every time you encounter a char, that char's dictionary value get's the index added
#Go through the dictionary and find the smallest gap between any chars. 