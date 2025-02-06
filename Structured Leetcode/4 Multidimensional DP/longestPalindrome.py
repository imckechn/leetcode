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
        x = 1

        while i-x >= 0 and i+x+1 < len(s):
            if s[i-x] != s[i+x+1]:
                break
            else:
                x += 1
        return x+1 #plus one for the value to the right

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s[0]
        
        largest = 1
        index = 0
        reflect = False

        for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                ans = Solution.getPalinSiblingsLen(s, i)
                if ans > largest: 
                    largest = ans
                    index = i
                    reflect = False

            if i+2 < len(s):
                if s[i] == s[i+2]:
                    ans = Solution.getPalinRelectLen(s, i, i+2)
                    if ans > largest: 
                        largest = ans
                        index = i
                        reflect = True

        pal = ""
    
        if not reflect:
            for i in range(1+index - largest//2, 1+math.ceil(index + largest/2)):
                pal += s[i]
            
        else:
            for i in range(index - math.floor(largest/2), math.ceil(index + largest/2)):
                pal += s[i]
            
        return pal
    



print(Solution.longestPalindrome(None, "acc")) #    cc
# print(Solution.longestPalindrome(None, "caba")) #    aba
print(Solution.longestPalindrome(None, "aaaa")) #    aaaa
print(Solution.longestPalindrome(None, "ccd")) #    cc
print(Solution.longestPalindrome(None, "cbbd")) #   bb
print(Solution.longestPalindrome(None, "ccccc")) #  ccccc
print(Solution.longestPalindrome(None, "ccc")) #    ccc
print(Solution.longestPalindrome(None, "ac")) #     a
print(Solution.longestPalindrome(None, "bb"))    #  bb
print(Solution.longestPalindrome(None, "babad")) #  bad or aba
print(Solution.longestPalindrome(None, "cbbd")) #   bb
print(Solution.longestPalindrome(None, "qwertyuiopoiuytrewq"))  #qwery both ways