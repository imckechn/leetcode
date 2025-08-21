import math


class Solution:
    def getPalinRelectLen(s, a, b):
        leftPointer = -1
        rightPointer = 1

        left, right = a, b

        while True:
            if a+leftPointer >= 0 and b+rightPointer < len(s):
                if s[a+leftPointer] == s[b+rightPointer]:
                    left = a+leftPointer
                    right = b+rightPointer

                    leftPointer -= 1
                    rightPointer += 1
                    continue
            break

        return left, right+1

    def getPalinSiblingsLen(s, i):
        leftPointer = -1
        rightPointer = 2

        left, right = i, i+1
        
        while True:
            if i+leftPointer >= 0 and i+rightPointer < len(s):
                if s[i+leftPointer] == s[i+rightPointer]:
                    left = i+leftPointer
                    right = i+rightPointer

                    leftPointer -= 1
                    rightPointer += 1
                    continue
            break

        return left, right+1

                

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s[0]
        
        start, stop = 0,1
        largest = 1

        for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                l, r = Solution.getPalinSiblingsLen(s, i)
                if r-l > largest: 
                    largest = r-l
                    start = l
                    stop = r

            if i+2 < len(s):
                if s[i] == s[i+2]:
                    l, r = Solution.getPalinRelectLen(s, i, i+2)
                    if r-l > largest: 
                        largest = r-l
                        start = l
                        stop = r

        pal = ""
    
        for i in range(start, stop):
            pal += s[i]
    
        return pal


print(Solution.longestPalindrome(None, "acc")) #    cc
print(Solution.longestPalindrome(None, "caba")) #    aba
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