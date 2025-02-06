import math


class Solution:
    def getPalinRelectLen(s, a, b):
        x = 0

        while a-x >= 0 and b+x < len(s):
            if s[a-x] != s[b+x]:
                return x + b
            else:
                x += 1

        return x + b - 1

    def getPalinSiblingsLen(s, i):
        x = 0

        while i+x+1 < len(s) and i-x >= 0:
            if s[i-x] != s[i+x+1]:
                break
            else:
                x += 2
        return x

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s[0]
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        
        largest = 1
        index = 0
        reflect = False

        for i in range(1, len(s)):

            if i < len(s)-1 and s[i-1] == s[i+1]:
                ans = Solution.getPalinRelectLen(s, i-1, i+1)
                if ans > largest: 
                    largest = ans
                    index = i
                    reflect = True

            if s[i-1] == s[i]:
                ans = Solution.getPalinSiblingsLen(s, i-1)
                if ans > largest: 
                    largest = ans
                    index = i
                    reflect = False

        pal = ""
    
        if reflect:
            for i in range(index - math.floor(largest/2), math.ceil(index + largest/2)):
                pal += s[i]
            
        else:
            for i in range(index - largest//2, math.ceil(index + largest/2)):
                pal += s[i]
            
        return pal
    



# print(Solution.longestPalindrome(None, "caba")) #    aba
print(Solution.longestPalindrome(None, "aaaa")) #    aaaa
print(Solution.longestPalindrome(None, "acc")) #    cc
print(Solution.longestPalindrome(None, "ccd")) #    cc
print(Solution.longestPalindrome(None, "cbbd")) #   bb
print(Solution.longestPalindrome(None, "ccccc")) #  ccccc
print(Solution.longestPalindrome(None, "ccc")) #    ccc
print(Solution.longestPalindrome(None, "ac")) #     a
print(Solution.longestPalindrome(None, "bb"))    #  bb
print(Solution.longestPalindrome(None, "babad")) #  bad or aba
print(Solution.longestPalindrome(None, "cbbd")) #   bb
print(Solution.longestPalindrome(None, "qwertyuiopoiuytrewq"))  #qwery both ways